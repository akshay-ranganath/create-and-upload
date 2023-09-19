import cloudinary.api

# create the 6 different named transformations necessary for Cineverse.
# ensure that the naming matches the names required by downstream systems.

transformations = {
    "text_removed": dict(
        effect="gen_remove:prompt_text;multiple_true"
    ),
    "logo_horiz": dict(
        background="gen_fill",
        width=2048,
        height=1536,
        crop="pad"
    ),
    "logo_square": dict(
        width=1080,
        height=1080,
        gravity="auto",
        crop="fill"
    ),
    "logo_vert": dict(
        width=2100,
        height=3000,
        gravity="auto",
        crop="fill"
    ),
    "nologo_horiz": dict(
        background="gen_fill",
        width=3840,
        height=2160,
        gravity="east",
        crop="pad"
    ),
    "nologo_vert": dict(
        background="gen_fill",
        width=768,
        height=1218,
        gravity="north",
        crop="pad"
    )
}

for tx in transformations:
    resp = cloudinary.api.create_transformation(tx, definition=transformations[tx])
    print(resp)