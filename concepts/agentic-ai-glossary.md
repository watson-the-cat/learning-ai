# Agentic AI Glossary

A reference guide written for data analysts, not engineers. These are the terms and concepts
you need to understand to talk about AI tools with confidence.

---

## The Big Picture: Chatbot vs Agent

### Chatbot
What most people think of when they say "AI." You type a question, it types an answer.
It's a conversation — the AI has no ability to *do* anything beyond generating text.

**Example:** Asking ChatGPT "How do I calculate ticket velocity?" and getting an explanation.

### Agent (Agentic AI)
An AI that can take **actions**, not just answer questions. It can read files, write code,
run commands, search databases, call APIs, and make decisions about what to do next — all
on its own, based on your instructions.

**Example:** Telling Cursor "Build me a chart showing ticket velocity from this CSV file"
and it writes the Python code, runs it, sees the error, fixes it, and produces the chart.

### The Key Difference
- **Chatbot:** You ask, it answers. You do the work.
- **Agent:** You describe what you want, it does the work. You review and give feedback.

Think of it like this:
- Chatbot = asking a colleague a question in Slack
- Agent = delegating a task to a teammate who goes and does it

---

## Core Concepts

### Tools / Function Calling
The way an agent interacts with the real world. An agent by itself can only generate text.
**Tools** give it hands — the ability to read files, run code, query databases, etc.

In Cursor, the agent has tools like:
- Read/write files on your computer
- Run terminal commands
- Search the codebase
- Access the web

**Why it matters:** The more tools an agent has, the more it can do autonomously.

### MCP (Model Context Protocol)
A standard way to give AI agents access to external tools and data sources. Think of it
as a universal adapter.

**Your Cursor setup already has MCP servers for:**
- **NVBugs** — query and search bug data
- **GitLab** — interact with NVIDIA's code repositories
- **Google Drive** — search and read your Drive files
- **OneDrive** — search and read OneDrive files
- **SharePoint** — search and read SharePoint documents

This means your Cursor agent can directly query NVBugs data, find files in your Drive,
or look up GitLab projects — without you needing to manually export/import anything.

### Context Window
The agent's working memory. Everything the AI can "see" at once — your conversation,
the files it's reading, tool results, its instructions. It has a fixed size limit.

**Why it matters for you:**
- If a conversation gets very long, the AI may "forget" things from earlier
- Starting a new conversation resets the context (fresh memory)
- This is why **skills and rules** exist — they automatically load important context

**Analogy:** It's like a desk. You can only have so many papers spread out at once.
Context window = desk size.

### Tokens
The unit of measurement for AI input/output. Roughly: 1 token ~ 0.75 words.
When people say "context window is 200K tokens," that's about 150,000 words of
combined input + output the AI can handle at once.

### Prompt Engineering
The skill of writing clear instructions for AI. But for agentic AI, the better
analogy is **product ownership** — you're not writing clever tricks, you're being
a clear communicator about what you want, what the constraints are, and what
good output looks like.

**Key principles:**
1. Be specific about what you want (not vague)
2. Give examples of good output when possible
3. State constraints upfront ("use this data source," "format as a table")
4. Iterate — first attempt is rarely perfect, and that's fine

### Hallucination
When AI generates something that sounds confident but is wrong. It's not lying —
it doesn't know the difference. It's pattern-matching and sometimes the patterns
lead to fabricated facts, incorrect code, or made-up data.

**How to protect yourself:**
- Always verify numbers and data against your source
- Be skeptical of specific claims (dates, statistics, API details)
- Test code by running it — don't just trust it
- The more specific your input data, the less room for hallucination

### Temperature
A setting that controls how "creative" vs "predictable" AI responses are.
- Low temperature (0) = very predictable, same answer every time
- High temperature (1+) = more creative, more varied, more risk of nonsense

For data analysis work, lower temperature is usually better (you want accuracy).

---

## Cursor-Specific Concepts

### Agent Mode vs Ask Mode
- **Agent Mode:** Cursor can read, write, and run code. Full autonomy. Use this when
  you want it to build or change something.
- **Ask Mode:** Read-only. Cursor can look at code and answer questions but can't
  change anything. Use this when you want to understand something without risk.

### Cursor Rules
Persistent instructions that automatically apply to every conversation in a project.
Stored in `.cursor/rules/` in your project folder.

**Example:** You could create a rule that says "I'm a data analyst, not an engineer.
Explain technical concepts simply. Always use Python with pandas for data work."
Every Cursor conversation in this project would then follow those preferences.

### Cursor Skills
Reusable instruction playbooks that teach the AI how to perform specific tasks.
More structured than rules — they include step-by-step workflows, templates,
and sometimes utility scripts.

**Two types:**
- **Personal skills** (`~/.cursor/skills/`) — available in all your projects
- **Project skills** (`.cursor/skills/`) — shared with anyone who opens the repo

**Example skill:** `analyze-nvbugs` — a skill that tells Cursor exactly how to
query NVBugs data, what fields to look at, and how to format the output.
Every time you or a colleague asks about NVBugs, the AI automatically follows
this playbook.

**Why skills matter:**
- You teach the AI once, it remembers forever (across conversations)
- You can share skills with teammates
- They're just markdown files — no coding required

**Analogy:**
- A **prompt** = telling a new hire what to do verbally, once
- A **rule** = posting a note on their desk they see every day
- A **skill** = writing it into the team procedures manual with examples

### Subagents / Task Tool
Cursor can launch specialized sub-agents to handle complex tasks in parallel.
Think of it as delegating parts of a big task to different specialists.

**Example:** You ask Cursor to analyze your codebase. It launches one subagent
to explore the backend, another to explore the frontend, and combines the results.

---

## Workflow Concepts

### The Feedback Loop
The most important pattern in agentic AI:

```
1. Describe what you want (plain English)
2. AI produces something (code, analysis, dashboard)
3. You review it (run it, look at the output)
4. You give feedback ("this chart is wrong because..." / "add a filter for...")
5. AI revises
6. Repeat until done
```

This is exactly how the ov-todo project was built — the product owner described
what they wanted, Claude built it, the owner gave feedback, Claude revised.

### Product Owner Mindset
The most effective way to use agentic AI as a non-engineer. You bring:
- **Domain knowledge** (what data matters, what metrics mean, what stakeholders need)
- **Requirements** (what the output should look like, what it should do)
- **Quality judgment** (is this right? is this useful?)

The AI brings:
- **Technical implementation** (writing code, configuring systems, building UIs)
- **Speed** (produces working code in seconds)
- **Breadth** (knows many languages, frameworks, and patterns)

You don't need to understand *how* the code works. You need to clearly describe
*what it should do* and judge *whether it did it correctly*.

---

## Pros and Cons of Agentic AI

### Pros
- **Speed:** Tasks that took hours can take minutes
- **Democratization:** Non-engineers can build tools, dashboards, automations
- **Handles boilerplate:** Repetitive coding, formatting, setup is automated
- **Cross-tool integration:** Can work across APIs, databases, file systems simultaneously
- **Learning accelerator:** Explains concepts while building — you learn by watching it work

### Cons
- **Hallucination risk:** Can produce wrong answers with high confidence
- **Verification burden:** YOU must check the output — don't trust blindly
- **Context limits:** Long conversations degrade quality; the AI may "forget" earlier context
- **Security considerations:** Agents with tool access can potentially modify important files
- **Cost:** API usage costs money (Cursor subscription, API tokens)
- **Dependency risk:** Over-relying on AI without building your own understanding
- **Non-deterministic:** Same prompt can produce different results each time

### Rules of Thumb
1. **Trust but verify** — especially for data analysis where accuracy matters
2. **Start small** — get one thing working before adding complexity
3. **Be specific** — vague requests get vague results
4. **Iterate** — first attempt rarely perfect, and that's fine
5. **Understand the output** — even if you didn't write the code, know what it does at a high level

---

## Git and Version Control Concepts

### Repository (Repo)
A project folder tracked by Git. Contains your code, files, and the full history
of every change ever made.

### GitHub vs GitLab
Both are platforms for hosting Git repos online. Same core concept, different platforms.
- **GitHub** — most popular public platform, good for personal/open-source projects
- **GitLab** — what NVIDIA uses internally, has built-in CI/CD

### Branch
A parallel version of your project. You create a branch to work on something
without affecting the main code. When you're done, you merge it back.

### Pull Request (PR) / Merge Request (MR)
A request to merge your branch into the main branch. This is where code review
happens. GitHub calls it a "Pull Request," GitLab calls it a "Merge Request."
Same concept.

### CI/CD (Continuous Integration / Continuous Deployment)
Automated processes that run when you push code:
- **CI:** Automatically tests your code to catch bugs
- **CD:** Automatically deploys your code to production

You don't need to set this up yourself right away — just know what people mean
when they say it.

---

## Quick Reference: AI Tool Landscape

| Tool | What it is | When to use |
|------|-----------|-------------|
| **Cursor** | AI-powered code editor (IDE) | Building projects, writing/editing code |
| **Claude CLI** | Claude in your terminal | Quick questions, scripting, automation |
| **ChatGPT / Claude web** | Browser-based chatbot | General questions, brainstorming |
| **GitHub Copilot** | AI code autocomplete | Inline code suggestions while typing |
| **Streamlit** | Python dashboard framework | Building web dashboards without HTML |
| **MCP Servers** | Tool adapters for AI agents | Giving AI access to NVBugs, GitLab, etc. |
