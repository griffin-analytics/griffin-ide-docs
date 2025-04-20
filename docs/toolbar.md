---
title: Dynamic Toolbar
---

# Dynamic Toolbar

Griffin Analytics Studio provides an optional and fully dynamic toolbar to be included in your custom IDE or tool. Please also see the documentation of the toolbar from a user point of view.

To enable the toolbar, simply include the Griffin Analytics Studio extension "@theia/toolbar" into your Griffin Analytics Studio-based product (also see the documentation on composing Griffin Analytics Studio applications).
*(Note: `@theia/toolbar` kept as technical detail)*

The Griffin Analytics Studio toolbar defines some default commands that are displayed even before the user can configure the toolbar to their preferences. These defaults are defined in a `ToolbarDefaultsFactory`. See the default `ToolbarDefaultsFactory` that is shipped within the toolbar extension for reference.
To define your own default commands to the toolbar, create a custom implementation of `ToolbarDefaultsFactory` and rebind you own factory in your extension module (see following code example).

```typescript
if (isBound(ToolbarDefaultsFactory)) {
  rebind(ToolbarDefaultsFactory).toService(MyCustomToolbarDefaultsFactory);
} else {
  bind(ToolbarDefaultsFactory).toService(MyCustomToolbarDefaultsFactory);
}
