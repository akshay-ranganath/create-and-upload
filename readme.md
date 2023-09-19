# Demo Files for Cineverse Workflow

The purpose of this simple project is to provide a quick pointer on the tools necessary to get you started. The core file is `demo_upload_and_download.py`. However, here is an overview all the files. If you would like to replay the project, please execute them in the order below.

1. create_named_transformations.py
2. create_upload_preset.py
3. demo_upload_and_download.py

## Step 1: Named transformation

[Named Transformations](https://cloudinary.com/documentation/image_transformations#named_transformations) are Cloudinary's mechanism to bundle a set of image manipulations and give it an easy to remember name. The first step is to create a set of named transforms based on the Cineverse requirements.

## Step 2: Upload Preset

Once the named transforms are defined, we create an [upload preset](https://cloudinary.com/documentation/upload_presets). Presets are like GitHub action - things that needs to be happen when a certain event fires. In our case, the event is the upload of an image. When an image is uploaded, we create a set of AI-based transformations. These transformations are defined using the _named transformations_ above.

## Step 3: Upload Images

The last step is to upload your images. When the images are uploaded, the upload preset (in step 2) will be used. So this will ensure that any image uploaded will be run through a process to create a set of transformations. These are the transformations defined in step 1.

## Other Considerations

The code assumes that you are uploading the files from an S3 location. To work with S3, you need to provide access for Cloudinary Uploader and place a file in `.wellknown/cloudinary/<your_cloud_name>`. For more information, please refer to [documentation page](https://cloudinary.com/documentation/upload_images#upload_from_a_private_storage_url).