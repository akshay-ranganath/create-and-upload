import cloudinary.uploader
import requests

# define your S3 bucket name here.
S3_BUCKET_NAME = "akshayranganath"

def get_file_name(url, transformation):    
    # transformation will be of the format "t_text_removed/jpg".
    # remove the "/jpg" part and the "t_" part
    transformation = transformation.rsplit('/',1)[0].split('t_',1)[1]    

    # from the URL, extract the file name. This will be of the format: 1000000010144_7GuardiansoftheTomb_portrait3x4.jpg
    # For this file name, insert the transformation from above as the last component in the file name
    file_name = url.rsplit('/',1)[1].replace('.jpg','')
    # if file name as the format s3_akshayranganath_, remove the prepended file name part
    # by default, Cloudinary will create the file name like s3_akshayranganath_1000000010144_7GuardiansoftheTomb_portrait3x4
    file_name = file_name.replace(f"s3_{S3_BUCKET_NAME}_","")
    file_name = file_name + '_' + transformation + '.jpg'
          
    print(file_name)
    return file_name

def download_and_save(url, file_name):
    # download the image and save it with the desired file name    
    resp = requests.get(url)
    with open(file_name, 'wb') as w:
        w.write(resp.content)

def delete_image(public_id):    
    # delete the image since transformation is now complete
    resp = cloudinary.uploader.destroy(
        public_id,
        type='upload',
        resource_type='image'
    )

def main():
    try:
        # upload the file. Create the necessary AI based deriviates inline.
        # no need to wait for any webhook notifications.
        print("Uploading and transforming image ..")
        resp = cloudinary.uploader.upload(
            f's3://{S3_BUCKET_NAME}/1000000010144_7GuardiansoftheTomb_portrait3x4.jpeg',
            upload_preset='ai_preset'
        )
        print("Done.")
        
        # response will contain the URLs for the transformations.
        # extract these URLs and download the images
        for transform in resp['eager']:
            tx = transform['transformation']
            url = transform['secure_url']
            file_name = get_file_name(url, tx)
            
            download_and_save(url, file_name)     
        
        print("Transformations downloaded successfully")
        
        # optional - delete the file once the transformations are download        
        delete_image(resp['public_id'])        
        print(f"Image {resp['public_id']} deleted successfully.")
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()