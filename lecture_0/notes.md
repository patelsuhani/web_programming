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
    - display (controls whether or not an element is visible)
* All CSS can be moved to a separate file with .css extension. This allows us to style multiple webpages of the same website within a single file/at a single location. 

* To link CSS file to HTML file:
    1. Use Link tag in head section of webpage.
    2. The relationship attribute (rel) is going to be "stylesheet" as what we are linking is a stylesheet for the page.
    3. Use href attribute to specify the hyperlink reference that is to be linked, in this case, a css file.

* By default, HTML uses a default size for everything on the page.
* To control the size of different elements, use width and height

* Use multiple element selector if different elements share the same style properties. You can list the elements seperated by commas before starting the style code. For example:

    `table, td, th{ border: 1px solid black; }`

* An ID is some unique name we give to an HTML element, so that we can reference it more easily later on.
* To style a particular element by its ID, reference it by a #. For example: `#foo{color: red;}`

* A class is a way of giving a name to an HTML element that might not be unique. For example: `<h1 class="bar">`
* To style everything with a particular class, use a dot. For example: `.foo{color: red;}`

* Specificity Order (decreasing):
    1. inline (takes precedence over everything)
    2. id
    3. class
    4. div

* Different CSS Selectors:
![CSS Selectors List](./css_selectors.jpeg)

* Pseudo class is a way of giving a name to an HTML element that might not be unique and to enable styling those elements in a particular way under certain conditions, for example, when you hover your mouse over it.

* **Responsive Design**:
    1. **Viewport**: The visual part of the screen that the user can actually see. To help adjust the size of the contents relative to the size of the screen of the device, you can use the following functionality:
    
    `<meta name="viewport" content="width=device-width", initial-scale=1.0">`
    This line of code is providing some metadata to out HTML page and saying, I would like you to change the width of the viewport to be specifically the width of the device.

    2. **Media Queries**: Help control how the page is going to look depending on how we render that particular page or what size screen we are rendering that page on. We can use this to check if a mobile device is vertical or landscape. We can see if the user is viewing the page on a computer screen or if they are trying to print the contents of the page as well.
    
    `@media (min-width: 600px){body{background-color: lightblue;}}`

    3. **Flexbox**: Helpful if we have multiple elements that we're all trying to display on the same page at the same time that might overflow if we're not careful about how we do responsive design. It can wrap the elements around using the flex-wrap property(changes the location where they are placed) to maintain their relative sizes across screens of different sizes.
    4. **Grids**: