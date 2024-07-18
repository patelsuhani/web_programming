# Lecture 0

## Overview

In this lecture, we'll be getting this cat to show up on a web page :)

![cat image](./cat.jpeg)

* To run the html file from VS Code, right click on the file in the filetree and select "Open with Live Server".

### HTML

* `div` tag:
    - Think of it as a division of the page or a section of the page.
    - 

### CSS
* CSS code is used for styling an HTML page.
* The style related information can be added as an attribute inside the body of the page.
* For better readability and convenient editing, the style related code can be moved to the header of the page inside of the style element.
* Within the Style element, you can specify the style information for different types of elements.
* Some common stype properties: color, text-align,
* All CSS can be moved to a separate file with .css extension. This allows us to style multiple webpages of the same website within a single file/at a single location. 

* To link CSS file to HTML file:
    1. Use Link tag in head section of webpage.
    2. The relationship attribute (rel) is going to be "stylesheet" as what we are linking is a stylesheet for the page.
    3. Use href attribute to specify the hyperlink reference that is to be linked, in this case, a css file.

* By default, HTML uses a default size for everything on the page.
* TO control the size of different elements, 