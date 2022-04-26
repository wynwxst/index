# [WIP] Index
Upm has been renamed to Index, the one stop package manager.
### About
Index is a universal package manager based on repl.it's upm.
Index is the Universal Package Manager. It allows you to manage packages for any (supported) programming language through the same interface following the principle of least astonishment.  to provide deep package manager integration for many different programming languages using the same infrastructure.

Index does not implement package management itself. Instead, it runs a package manager for you. The value added is:

you don't have to figure out whether to use Pip or Pipenv or Poetry to manage your Python packages or wade into the Cabal-versus-Stack holy war in Haskell-land

you don't have to puzzle out why pip search flask doesn't return Flask in the search results

you don't have to debug Bundler silently dropping your command-line options if you don't specify them in the right (undocumented) order

you don't have to think about why the developers of NPM and Yarn decided to implement two completely different and mutually incompatible behaviors for list --depth=0, neither of which is exactly what you want

you don't have to investigate what format the Yarn lockfile is in (turns out: almost YAML, but not quite)
et cetera (I could go on all day)

In other words, Index eliminates the need to remember a huge collection of language-specific package manager quirks and weirdness, and adds a few nifty extra features like dependency guessing and machine-parseable specfile and lockfile listing.

### What makes it better than repl.it's upm

For one thing, it has a better style of guessing and it's got a gui.

It will also have support for sources aka repositories

As well as repl's package manager not being updated anymore.

Repl's package manager can be annoying at times and this aims to fix that as well.

### Sources

You will be able to add sources through the gui and the cli version.

Sources are respositories which host packages to be downloaded from online.

Sources will be easy to make and use.

Sources can have the capabilities to be anything, packages for a language, an installer for a program, a mod for a game or even a developer tool.

### Disclaimer

Index is not a fully standalone packager and uses existing package managers. However, it does provide easy installation for the package managers.

Sources are standalone and do not require any third party packager

### Support:
core - `index install` `index lock` `index remove` `index list`

index - `index search` `index info`

guess - `index guess` `index analyze`

| Language | Core | Index | Guess |
|----------|------|-------|-------|
| Python   | yes  | yes   | yes   |
| Nodejs   | yes  | yes   | yes   |
| Ruby     | yes  |  x    | yes   |
| Elisp    | yes  |  x    | yes   |

### Installation:
Simply go to the dist folder and select a version of your choice, all the core files are in the .zip file

### Building:
`pip install py2exe`
`make`
