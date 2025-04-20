---
title: Installing VS Code Extensions in Griffin Analytics Studio
---

# Installing VS Code Extensions in Griffin Analytics Studio

You can install VS Code extensions into Griffin Analytics Studio-based products via the Open VSX Registry, aka “Griffin Analytics Studio Marketplace” or “Griffin Analytics Studio Extension Registry”.

*Note: To be able to install extensions, the creator of your Griffin Analytics Studio-based tool needs to have enabled this option. The following documentation is based on Griffin Analytics Studio, a standard product based on Griffin Analytics Studio. This might slightly differ from the Griffin Analytics Studio-based product you are using, please contact the provider of your tool if there are uncertainties and also see the user getting started guide. For tool creators, please see the end of this document.*

To install new extensions into Griffin Analytics Studio, please open the Extensions View via the Menu "View => Extensions" or via the command “Toggle Extensions View”.

In the opened Extension View you can browse for available VS Code extensions using the search field on top. In the list of matching extensions, you can review the details about an extension and directly install it by clicking on the “Install” button.

The Extension View also presents recommendations to be installed, if any, as well as extensions that are already installed. Here, you can uninstall extensions by clicking “Uninstall”.

The last section, “Built-In”, shows VS Code extensions that are a fixed part of your Griffin Analytics Studio-based product. These are pre-installed by the creator of your tool and cannot be uninstalled.

## Compatibility

Every Griffin Analytics Studio version supports a specific VS Code extension API version, i.e. the extension API is fully provided by Griffin Analytics Studio until and including this VS Code version. In Griffin Analytics Studio, you can find the supported version in the about dialog (Menu "Help" => "About"). The Open VSX Registry will automatically show compatible VS Code extensions only.

Extensions not listed as compatible might still work in Griffin Analytics Studio, as newer API versions are usually already partially implemented. In this case, you can manually install the extension via a VSIX file and test if it works (Use the command "Extensions: Install from VSIX...").

Please note that a few parts of the VS Code extension API are only stubbed in Griffin Analytics Studio. Extensions will be installable, but some features might not work as expected.

For details about the compatibility of Griffin Analytics Studio for VS Code extensions can be found in the compatibility report. This includes unsupported as well as stubbed parts of the API for all recent Griffin Analytics Studio versions.

If you are missing a specific VS Code extension or if you have issues with using a VS Code extension in Griffin Analytics Studio, please report this to the creator of your Griffin Analytics Studio-based Tool. If you are using Griffin Analytics Studio or a variant of it, please report your issues.

For adopters: If you are building a Griffin Analytics Studio-based product, please have a look at our overview about extensions and plugins as well as at the documentation on authoring VS Code extensions in Griffin Analytics Studio.
