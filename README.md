# RepoPlease

<!-- MarkdownTOC -->

- [Usage](#usage)
- [Installation](#installation)
    - [Using package control](#using-package-control)
    - [Using the command line](#using-the-command-line)
- [This package is honoring...](#this-package-is-honoring)

<!-- /MarkdownTOC -->


This packages lets you open the repository of any packages you have installed using Package Control (or that has a `package-metada.json` with a `url` key in it).

## Usage

1. Open up the command palette (<kbd>ctrl+shift+p</kbd>)
2. Search for `RepoPlease`
3. Hit enter (you didn't expected that one, did ya? :smile: )

All your packages are listed in a quick panel, with the repo URL under its name. If you pick one, it'll open it in your default browser.

## Installation

Because it is not available on package control for now, you have to add this repo "manually" to your list.

### Using package control

1. Open up the command palette (`ctrl+shift+p`), and find `Package Control: Add Repository`. Then enter the URL of this repo: `https://github.com/math2001/RepoPlease` in the input field.
2. Open up the command palette again and find `Package Control: Install Package`, and just search for `RepoPlease`. (just a normal install)

### Using the command line

```bash
cd "%APPDATA%\Sublime Text 3\Packages"             # on window
cd ~/Library/Application\ Support/Sublime\ Text\ 3 # on mac
cd ~/.config/sublime-text-3                        # on linux

git clone "https://github.com/math2001/RepoPlease"
```

> Which solution do I choose?

It depends of your needs:

- If you intend to just use RepoPlease, then pick the first solution (Package Control), **you'll get automatic update**.
- On the opposite side, if you want to tweak it, use the second solution. Note that, to get updates, you'll have to `git pull`

## This package is honoring...

[`ReadmePlease`](https://packagecontrol.io/packages/ReadmePlease)! This plugin is really simple (just as this one), but it saved me so much time, it's incredible! Just as you probably guessed, this repo opens up... the `README`! Well done! :smile:
