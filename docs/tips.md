---
title: Advanced Tips
---

# Advanced Tips

In this section we'll outline some advanced hints and tips to get the most out of developing tools based on Griffin Analytics Studio.

## Providing custom API to VS Code extensions in Griffin Analytics Studio

Griffin Analytics Studio allows running VS Code extension by providing a compatible API (see the overview for details).
It is possible to extend this API to allow VS Code extensions running in Griffin Analytics Studio to access additional functionality compared to when they run within VS Code.
This allows you to provide a feature as a VS Code extension targeting VS Code and Griffin Analytics Studio. However, when running in Griffin Analytics Studio, the feature can be enhanced by using custom API only available in Griffin Analytics Studio.

The following code example shows the usage custom API which is invoked only when running in a Griffin Analytics Studio-based application. This is determined via the application name.
The API is imported asynchronously to avoid runtime errors in VS Code.

```typescript
if (vscode.env.appName === MY_GRIFFIN_APP_NAME) { 
    // Implement Griffin Analytics Studio API
    const api = await import('@mygriffinextension/mycustomapi'); 
    // After importing the custom API, it can be used as any other API. The following lines are using an example API.
    api.host.getMessageHandler(() => getMessage());
    api.host.onRequestMessage((actor: string) => {
        const message = getMessage(actor);
        api.host.showMessage(message);
    });
}
```
*(Note: Assumed application name `MY_GRIFFIN_APP_NAME` and package path `@mygriffinextension/mycustomapi`, adjust if different)*

An alternative to providing a custom API is to define custom commands. Again, these commands would only be available if the VS Code extension is running in Griffin Analytics Studio (see following code example).

```typescript
if (vscode.env.appName === MY_GRIFFIN_APP_NAME) { 
    // Execute Griffin Analytics Studio custom command
    const commands = await vscode.commands.getCommands();
    if (commands.indexOf(MY_GRIFFIN_CUSTOM_COMMAND) > -1) { 
        vscode.commands.executeCommand(MY_GRIFFIN_CUSTOM_COMMAND); 
    }
}
```
*(Note: Assumed application name `MY_GRIFFIN_APP_NAME` and command `MY_GRIFFIN_CUSTOM_COMMAND`, adjust if different)*

An example of this technique can be seen in related projects.
