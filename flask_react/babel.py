import os


def install():
    """Installs babel for JSX conversion."""
    cmd = "npm install --save-dev " \
          "babel-cli " \
          "babel-plugin-transform-react-jsx " \
          "babel-plugin-transform-es2015-arrow-functions "
    os.system(cmd)


def convert(
        jsx: str = os.path.join("static", "react", "jsx"),
        js: str = os.path.join("static", "react", "js")
):
    """Convert JSX files to JS.

    :param jsx: Path to directory containing JSX files.
    :param js: Output directory.
    """
    os.system(f"{os.path.join('node_modules', '.bin', 'babel')} "
              f"--plugins "
              f"transform-react-jsx,transform-es2015-arrow-functions "
              f"{jsx} "
              f"--out-dir {js} ")
