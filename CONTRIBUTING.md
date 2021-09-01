The following contributing guide has been inspired by [flask](https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst) and 

# Contributing guide

Thank you for your interest in contributing to our repository. We welcome contributions in the form of bug reports, documentation  pull requests. Following are certain guidelines and instructions to follow while making your contribution.

## Reporting issues

Use github issues for reporting bugs and make sure your post follows details:
- Present a [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) of your issue and remove any unnecessary details
- Make sure to use the latest release of the library to avoid reporting bugs that were fixed in later releases
- Optionally, add your device configuration information

## Updating / Adding documentation

For suggesting minor changes to documentation(typos, etc.) use the Edit button✏️ in Github to make the change and click "Propose Changes" to submit it for review.

For adding new pages, fork the repo, create a branch and submit it as a PR

## Code contributions

### Getting Started

Make sure you have 

Follow these steps to get __ setup on your local machine
- Fork the _ repository to your own Github account 
- Clone the repository

        $ git clone https://github.com/Neelkanth7/TUSK
        $ cd TUSK
- Add your fork as remote to push your work to
- Create a virtual environment and install the required dependencies
- Run setup
- Testing. TBD
- When ready to submit, raise a pull request and describe the feature/bug fix thoroughly in the description. Also add a link to the issue if relevant

### Commit guide

All commit messages must follow the [conventional commit specification](https://www.conventionalcommits.org/en/v1.0.0/). This helps others to easily understand commit logs and allows for automated changelog generation. Here's an example of a commit message that follows the conventional commit spec

    feat: allow provided config object to extend other configs

In general, the messages must follow the following syntax

    <type>[optional scope]: <description>

    [optional body]

    [optional footer(s)]