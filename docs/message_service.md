---
title: Message Service
---

# Message Service

The message service allows you to show messages, interactive dialogues and progress information to the user. You can get the `MessageService` injected and call either `info`, `warn` or `error` on it to report your message (see code example below):

```typescript
@inject(MessageService) private readonly messageService: MessageService
this.messageService.info('Hello World!')
```

By default, Griffin Analytics Studio will display messages as toast notifications in the bottom right corner. Please note that you can easily adapt Griffin Analytics Studio to implement a different behavior for displaying messages by providing a custom `MessageClient`.

By default, notifications will be displayed until the user closes them. You can optionally define a time-out after which messages will be closed automatically:

```typescript
this.messageService.info('Say Hello with timeout',{timeout: 3000})
```

Optionally, you can also add actions that the user can execute. In case the user executes an action, the message service call will resolve to the action string which was handed over.

In the following code example, we provide the two actions “Say Hello again!” and “Cancel”. We react to the action “Say hello again!” by posting yet another message, “Cancel” will be ignored.

```typescript
@inject(MessageService) private readonly messageService: MessageService

this.messageService
 .error("Hello World!", "Say Hello again!", "Cancel")
 .then((action) => {
   if (action === "Say Hello again!")
     this.messageService.info("Hello again!");
   })
```

The corresponding toast notification will show the message and buttons for the actions.

When the user selects “Say Hello again”, another toast notification will be shown.

## Progress Reporting

The message service also allows you to report progress on an ongoing operation. You can incrementally update a progress bar and the message while the toast notification remains visible until the operation is done. The following example opens a progress bar and updates the status three times before it is completed. Please see the TypeDoc of `MessageService` for more detailed information.

```typescript
this.messageService
 .showProgress({
   text: `Doing something`,
 })
 .then((progress) => {
   // Do something
   progress.report({
     message: "First step completed",
     work: { done: 10, total: 100 },
   });
   // Do something
   progress.report({
     message: "Next step completed",
     work: { done: 80, total: 100 },
   });
   // Do something
   progress.report({
     message: "Complete",
     work: { done: 100, total: 100 },
   });
   progress.cancel();
 })
```

Note that `progress.cancel` is also used to signal that progress is complete.
The code example above will display a progress notification that updates accordingly.
