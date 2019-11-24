# Flask-React
React extension for Flask applications with support for multiple add-ons.

##Usage

To initialize Flask-React, simply create a `React` instance and provide the 
Flask instance. Additional parameters:
 - `index_template` : Index page template to use instead of default one.
 - `extensions` : List of React extensions to use. Currently Material-UI, 
 React-Bootstrap and Socket.IO are available.
 - `jsx_folder`: Source folder for JSX files. If provided, .jsx files are 
 converted using Babel on initialization.
 - `socket_io`: Flask-SocketIO instance (socket.io is used).
 
 ```python
from flask import Flask
from flask_react import React


app = Flask(__name__)
react = React(
    app,
    extensions=("material", "components"),
    jsx_folder='static/react/jsx/'
)


if __name__ == '__main__':
    app.run()
```

The React code goes into the `static\react\js` folder, or if you use JSX, the 
folder you provided at initialization. The `App.js` file must contain an `App` 
function that returns the contents of our application.

```js
function App() {
  return React.createElement(
    "div",
    null,
    "Hello world!"
  );
}
```
If you use JSX, your `App.jsx` would look something like this:
```jsx harmony
function App() {
  return (
      <div>Hello world!</div>
  )
}
```
Additional files that should be put in the `static/react/` folder are:
- `favicon.ico`
- `logo192.png`, `logo512.png`
- `manifest.json`
