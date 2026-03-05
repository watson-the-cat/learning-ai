# Learning Progress Log

This file tracks what's been done and where to pick up if starting a new conversation.

## Completed

### Phase 0: Setup (March 4, 2026)
- Installed Python 3.12 (located at `$env:LOCALAPPDATA\Programs\Python\Python312\python.exe`)
- Git was already installed (v2.53.0)
- Created GitHub account: watson-the-cat
- Created public repo: https://github.com/watson-the-cat/learning-ai
- Initialized local git repo in this workspace
- Created folder structure (concepts/, cheatsheets/, projects/)
- Created starter files: README.md, .gitignore, cheatsheets, AI glossary
- First commit and push to GitHub

### Phase 1: Terminal and Git Basics (March 4, 2026)
- Practiced full git workflow: add, commit, push (multiple times)
- Learned branching: create, switch, merge, delete
- Key lesson: save files (Ctrl+S) before `git add`
- Key lesson: branches only exist on GitHub if you push them there
- Key lesson: commit saves locally, push uploads to GitHub — they're separate steps

### Phase 2: Agentic AI Concepts (March 4, 2026)
- Covered: chatbot vs agent, MCP/MaaS, context window, tokens, hallucination, product owner mindset
- Covered: evolution of AI (autocomplete > chatbot > chatbot+tools > agent)
- Covered: how transformers, RLHF, and function calling enabled the leap
- Covered: practical strategies for verification (small chunks, explain-first, test with known data)
- Key takeaway: AI handles the tedious 70%, you focus on the critical 30%
- Glossary file: concepts/agentic-ai-glossary.md

### Phases 3 & 4: First Dashboard (March 5, 2026)
- Built a Streamlit dashboard for CSP cloud usage data (32K rows)
- Data file: projects/first-dashboard/combined_csp_data.csv (gitignored)
- Dashboard code: projects/first-dashboard/dashboard.py
- To run: `& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m streamlit run dashboard.py`
- Charts: GPU hours over time, customer trends, instance breakdown, product mix, % breakdown, top-N customers
- Filters: date range, cloud provider, product, GPU model, instance type, company, country
- Installed Python packages: streamlit, pandas, plotly
- Practiced the product owner feedback loop: requirements > build > review > iterate
- QA'd data against known sources
- Key lesson: Streamlit auto-refreshes on file save — no restart needed
- Key lesson: localhost is local only — no data leaves your machine

### Key Concepts Learned
- **Git** is a save-point system (add, commit, push)
- **Staging area** = selecting which changes; **commit** = saving the snapshot
- **Agent vs chatbot** = agents take actions, chatbots just answer
- **MCP** = connects agents to external systems (NVBugs, GitLab, Drive, etc.)
- **MaaS** = NVIDIA's hosted MCP servers
- **Context window** = agent's working memory (has a limit, oldest stuff falls off)
- **Tokens** = how AI reads text (word fragments, like Lego bricks)
- **Hallucination** = AI being wrong while sounding confident; always verify
- **Skills** = reusable instruction playbooks for AI (SKILL.md files)
- **Cursor rules** = persistent instructions that apply to every conversation in a project
- **Product owner mindset** = define requirements, provide domain knowledge, review output, give feedback

### Git Commands Practiced
- `cd`, `ls`, `git status`, `git diff`, `git log --oneline`
- `git add`, `git commit -m`, `git push`
- `git config --global`
- `git checkout -b`, `git checkout`, `git branch`, `git merge`

## Important Rules
- **No NVIDIA data on GitHub.** Data files are gitignored. Cursor rule enforces this (.cursor/rules/data-safety.md)
- Code goes to GitHub, data stays local
- `python` is not in PATH — use full path: `$env:LOCALAPPDATA\Programs\Python\Python312\python.exe`

## Pending / Next Up

### Phase 5: GitLab + Live Data
- Set up a project on NVIDIA GitLab
- Learn GitLab workflow (branches, merge requests)
- Connect dashboard to live data (NVBugs, Databricks)
- Learn about deploying to internal NVIDIA infrastructure

### Phase 6: Advanced Agentic Patterns
- Claude CLI
- MCP in depth (chaining tools together)
- Cursor Rules and Skills (creating custom ones)
- Multi-agent patterns
- Evaluating AI tools

### Open Items from Last Session
- Kevin wanted to walk through dashboard.py to understand the code section by section
- Kevin noted Python can't do much without importing libraries — worth discussing imports and packages
- Future: look into deploying Streamlit to internal NVIDIA site (like ov-todo.nvidia.com)
- Future: add GitHub MCP server when needed
