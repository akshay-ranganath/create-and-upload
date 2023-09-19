import cloudinary.api

# bundle the named transformations created earlier into one upload preset.
# this will be used during upload for generating all the necessary transformations
resp = cloudinary.api.create_upload_preset(
    name="ai_preset",
    unique_filename=False,
    use_filename=True,
    overwrite=False,
    eager = [               
        {
            "transformation": "text_removed",
            "format": "jpg"            
        },
        {
            "transformation": "logo_horiz",
            "format": "jpg"
        },
        {
            "transformation": "logo_square",
            "format": "jpg"
        },
        {
            "transformation": "logo_vert",
            "format": "jpg"
        },
        {
            "transformation": "nologo_horiz",
            "format": "jpg"
        },
        {
            "transformation": "nologo_vert",
            "format": "jpg"
        }    
    ],
    eager_async=False    
)
print(resp)

#on_success="current_asset.update({tags: ['autocaption']});"
#eager_notification_url="https://webhook.site/2526ac30-a2ff-4980-97b3-2dfc35904353",