# ImgGenCli : Image Generation 💠

`imggencli` is a community-maintained cli designed to provide users with the ability to generate, edit and filter images using the DALL-E 2 API provided by OpenAI, all from the command line interface.

The tool provides three main commands, generate, edit, and filter.

Test-101

The `generate` command allows the user to generate an image using a prompt, with the option to apply a filter, specify the size, and choose the number of times to generate the image. The generated image can also be saved to a specified file path.

The `edit` command provides the ability to edit an existing image by adjusting the brightness, contrast, and sharpness of the image. The edited image is then saved to a new file.

The `filter` command allows users to apply various filters and effects to an existing image. The user can select from a range of different filters, and the filtered image can be saved to a specified file path.

Thus it allows for a low end build that can work on almost all computers with high sense of flexibility with it's customization options.

## Configuration

The cli requires you to have an api token to query the OpenAI's api. You can read about and get it here https://platform.openai.com/account/api-keys.

## Installation

Install the imggencli python package directly from pypi. 

```console
  pip install imggencli
```

## Usage

```console
Usage: imggencli [OPTIONS] COMMAND [ARGS]...

  💠 Use the Dall.E 2 api to generate, edit & filter images from the cmd line.

Options:
  --help  Show this message and exit.

Commands:
  edit      🎴 Change the brightness, contrast and sharpness of an image.
  filter    🦄 Apply filters and effects to an image.
  generate  🌸 Generate an image from the OpenAI Dalle api.
  img2img   🖼️ Generate a variation of an image from an existing image.
  update    🔐 Update the OpenAI API key.
```

### Commands and Options

**```generate```**
```console
Usage: imggencli generate [OPTIONS]

  🌸 Generate an image from the OpenAI Dalle api

Options:
  --prompt TEXT                   💬 The prompt to generate the image from.
  --size TEXT                     📐 The size of the generated image.
  --filter                        🎨 Apply a filter to the generated image.
  --iterations INTEGER            🔄 The number of times to generate the image
  --save-path FILE                💾 Save the generated image to the specifiedfile path
  --help                          Show this message and exit.
```

**```edit```**
```console
Usage: imggencli edit [OPTIONS] IMAGE_PATH

  🎴 Change the brightness, contrast and sharpness of an image.

Options:
  --brightness FLOAT  💡 The brightness of the image
  --contrast FLOAT    🌈 The contrast of the image
  --sharpness FLOAT   🔪 The sharpness of the image
  --help              Show this message and exit.
```

**```filter```**
```console
Usage: imggencli filter [OPTIONS] IMAGE_PATH

  🦄 Apply filters and effects to an image.

Options:
  --filter [grayscale|sepia|blur|contour|detail|edge_enhance|edge_enhance_more|emboss|find_edges|sharpen|smooth|smooth_more|outline|posterize|solarize|invert|flip]
                                  🎨 The filter to apply to the image
  --save-path PATH                The directory to save the filtered image.
                                  Defaults to the current directory.
  --help                          Show this message and exit.
```

**```update```**
```console
Usage: imggencli update [OPTIONS]

  🔐 Update the OpenAI API key.

Options:
  --help  Show this message and exit.
```

**```img2img```**
```console
Usage: imggencli img2img IMAGE_PATH

  🖼️ Generate a variation of an image from an existing image.

Options:
  --help  Show this message and exit.

```


### Drawbacks as of now : 
- Image variation strictly needs a square image of a Square dimension.
- Image variation requires only a PNG image of depth 24 bit. Other formats will have to be converted into a 24 bit PNG square image.
- Image variation is not very accurate and can be improved upon. Accuracy has been kept low to facilitate use of the app on low end devices as well.
- Quality of images may not be the best to again ensure not only heavy performing but every device can run the app.
