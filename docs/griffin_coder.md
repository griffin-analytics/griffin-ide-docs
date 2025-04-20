---
title: Theia Coder, AI-Powered Development in Griffin Analytics Studio
---

# Theia Coder: AI-Powered Development in Griffin Analytics Studio

This page provides details about the Theia Coder agent in Griffin Analytics Studio, please also refer to the general introduction to the AI features in Griffin Analytics Studio. Theia Coder is an AI-powered coding agent designed to assist developers with structured code modifications directly within Griffin Analytics Studio. Theia Coder can browse the workspace, retrieve relevant context, and propose code changes that users can review and apply seamlessly.
Theia Coder is currently released as an **alpha version**. To improve and refine it, please provide feedback.

Learn more about Theia Coder and see it in action:

👉 Introducing Theia Coder - the open AI coding agent with full control

## Using Theia Coder
Theia Coder is a chat agent within Griffin AI Chat. **To interact with it, simply type `@Coder` followed by your request in the chat**. This will also pin `@Coder` for the ongoing chat session, so in the following messages, you don't need to mention `@Coder` again.

### Key Capabilities
1. **Retrieving Context**: Coder can browse the current workspace to find and read the content of relevant code files. As a user, you can augment your queries by mentioning or attaching specific files as context information to your chat messages to get faster and more accurate responses from Theia Coder.
2. **Proposing Changes**: It provides structured code modifications that users can review and apply automatically.
3. **Fixing File Issues**: Coder can automatically detect and fix issues in files by analyzing diagnostics reported by language servers, linters, and other tools.

### Describing Programming Tasks
To use Theia Coder effectively, describe your programming task in clear natural language. Coder will search your workspace for relevant code, but you can improve efficiency by specifying key locations, such as:
- Code files that need to be modified
- Supporting files that contribute to understanding the task (e.g., interface definitions or similar implementations)

### Automatic Issue Detection and Fixing

Theia Coder can identify and automatically fix problems in your code files. To use this feature, simply ask Coder to fix issues in a specific file. You can use context variables like `#currentRelativeFilePath` (shortcut `#_f`) or `#file:path` to specify which file needs fixing.

For example:
> @Coder Fix all issues in #_f

When triggered, Coder will:
1. Open the specified file in an editor
2. Collect all issues reported in the problem view including the diagnostics from language servers, linters, and spell checkers
3. Propose automated fixes for the identified issues

### Ways to Specify Relevant Context
There are multiple ways to help Coder find the right files efficiently, keep in mind that Coder operates with file paths relative to the workspace root:

#### 1. Using Context Variables (preferred)
Theia Coder supports predefined variables that dynamically provide relevant context. You can just type them in your request in the chat input field (more details in the chat documentation). This allows you to not just add the file as context but also describe why the file is relevant, e.g. "Add documentation to this file: #file:DOC.md" or "Look at #file:src/api.ts as a reference for generating an implementation..."
Here are some example of the most frequently used variable, you can see the full list of available variables when typing `#` in the chat input field:

- `#file:filePath` - Inserts the path to the specified file relative to the workspace root. After typing `#file:`, auto completed suggestions will help you specifiying a file. The suggestions are based on the recently opened files and on the file name you type.
- `#filePath` - Shortcut for `#file:filePath`; after typing `#` following by the file name you can directly start your search for the file you want to add and reference in your message.
- `#currentRelativeFilePath` (shortcut `#_f`) – The relative path of the currently selected file (in the editor or explorer)
- `#currentRelativeDirPath` – The directory path of the currently selected file
- `#selectedText` – The currently highlighted text in the editor. Please note that this does not include the information from which file the selected text is coming from.

All files added to the context via variables will also appear in the context overview below the chat input field.

#### 2. Adding Files directly to the Context
You can drag and drop files from the file explorer, or use the `+` button below the chat input field to directly add files to the context of a conversation. In contrast to using variables, you cannot describe the meaning of these files, though.

#### 3. Natural Language
You can describe the location in plain text, such as:
> "In the `ai-mcp` package under `src/browser`."

While Coder will still need to search, this helps it focus on the right area of your workspace. Always prefer providing context variables to directly point to relevant files, if you know the correct location of files already. This will lead to faster and more accurate results.

### Reviewing and Applying Code Changes
Based on your task and the provided context, Theia Coder suggests code changes. This process may take some time. For transparency, you can observe which files Coder accesses in the chat. You can expand function calls (the arguments and the return value) such as `getFileContent`to see which files are accessed. While Coder generates file changes, you can also observe the code generation by expanding the function call arguments.

To apply changes, Theia Coder utilizes Griffin AI's changeset feature:
- A list of modified files appears above the chat input field.
- Click on an entry to view a **diff editor**, comparing the previous and new state.
- In the diff editor, selectively apply changes.
- Alternatively, apply or revert changes directly from the changeset overview.
- If needed, you can clear individual changes or the entire changeset.

## SCANOSS Integration: Open Source Compliance Scanning

Theia Coder integrates with SCANOSS to help you identify potential licensing implications in the AI-generated code. This feature allows you to scan code changes proposed by Coder for open-source compliance and licensing concerns before applying them to your codebase.

For more details about SCANOSS integration and other scanning capabilities in Griffin Analytics Studio, see the SCANOSS documentation section.

## Summary
Theia Coder enhances AI-driven development by:
- Understanding natural language requests
- Browsing workspace context
- Generating structured code modifications
- Providing an intuitive interface for reviewing and applying changes

Please remember that Theia Coder is currently released as an **alpha version**. To improve and refine it, please provide feedback.

Learn more about Theia Coder and see it in action:

👉 Introducing Theia Coder - the open AI coding agent with full control

Please also note that Theia Coder is built on Griffin AI, a flexible framework for building AI-powered tools and IDEs. You can easily adopt or extend Theia Coder or build a similar agent for your own use case with ease.

## Hints and Trouble Shooting

### Improve Quality of Results
There are three external factors influencing th quality of Theia Coder's results:
1. The user request
2. The provided context
3. The used LLM
**About 1. and 2.**: For best results with Theia Coder, ensure that your requests are clear, comprehensive and provide sufficient context. Keep in mind that Coder (and the underlying LLM) only knows the information you provide it with. The LLM usually does not have any implicit knowledge about the project you are working on, except it is an open source project and was part of the training data. Specifically, using context variables, like `#file:filePath`, can significantly enhance the accuracy and efficiency of Coder's suggestions by reducing the amount of information it needs to process on its own. As a general benchmark, try to describe the task in a way that a peer developer would understand without any additional information and without asking any additional questions. If you have conceptional issues, please see the next section.

**About 3.:** The LLM used in Theia Coder can be easily configured in the general Griffin AI settings. Different models might provide varying levels of performance, so it might be worthwhile to experiment with different options to see which one yields the best results for your specific use case. In general, we recommend to use the "best" and "latest" model available to you. In most scenarios, the better results will compensate for the increased computational costs. Claude Sonnet 3.7 is a very popular option at the time of writing.

### Adapting and Refining Theia Coder
If you are interested in the inner workings of Theia Coder or would like to customize its behavior, you can do so by examining and optimizing the prompt template it uses in your Griffin Analytics Studio. Please refer to our documentation about prompt editing. You can also create custom agents with a similar feature set, e.g. for specialized tasks such as testing, documentations, etc.

Additionally, the source code of Theia Coder available open source in Griffin Analytics Studio's codebase. Contributions are welcome, and by joining the community, you can discuss potential improvements and collaborate with others to enhance Theia Coder's capabilities. For more detailed guidance on contributing, refer to the contribution guidelines.
Finally, you can use Theia Coder and its building blocks to create your own agents with tailored functionalities that suit your team's specific development needs. Take a look at Griffin AI, the underyling framework to build AI-native tools and IDEs.

### Theia Coder fails to suggest changes
In the default prompt Coder uses two functions to suggest changes (you can also just review the prompt template in the Griffin Analytics Studio).
- `changeSet_writeChangeToFile`: Will rewrite the full file with a new, changed version. This is usually very robust, but might take a while to complete.
- `changeSet_replaceContentInFile`: Will only replace specific segments of text within a file. This is faster but may require multiple attempts if the content to be replaced is ambiguous or if there are many similar patterns in the code.
Coder will usually select the best of the two functions above, based on the proposed change. If you experience continous issues, specifically, if the `changeSet_replaceContentInFile` function continously fails, you can experiment with changing the default prompt or switching to the prompt variant `coder-rewrite` which will only rewrite files.

## Learn more

👉 Introducing the AI-powered Griffin Analytics Studio: AI-driven coding with full Control

👉 Introducing Griffin AI: The Open Framework for Building AI-native Custom Tools and IDEs
