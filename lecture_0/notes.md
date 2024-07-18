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
* Some common stype properties: 
    - color
    - text-align
    - background-color
    - width
    - height
    - padding (space inside of the border of the element)
    - margin (space outside of the border of the element)
    - font-family
    - font-size
    - font-weight
    - border (can specify how big, type of line, and color of line) 
    - border-collapse
* All CSS can be moved to a separate file with .css extension. This allows us to style multiple webpages of the same website within a single file/at a single location. 

* To link CSS file to HTML file:
    1. Use Link tag in head section of webpage.
    2. The relationship attribute (rel) is going to be "stylesheet" as what we are linking is a stylesheet for the page.
    3. Use href attribute to specify the hyperlink reference that is to be linked, in this case, a css file.

* By default, HTML uses a default size for everything on the page.
* To control the size of different elements, use width and height

* Use multiple element selector if different elements share the same style properties. You can list the elements seperated by commas before starting the style code. For example:

    `table, td, th{ border: 1px solid black; }`

* 