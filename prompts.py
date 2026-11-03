from langchain_core.prompts import ChatPromptTemplate

# Agent 1: Groq
security_prompt = ChatPromptTemplate([
    ("system", "You are Agent 1: Principal Security Auditor. Scan the git diff ONLY for vulnerabilities "
               "(SQL/NoSQL injection, missing auth, exposed secrets, XSS, unsafe inputs). "
               "Specify exact line numbers and concrete replacement fixes. If clean, output 'NO_ISSUES'."),
    ("human", "File: {file_path}\nDiff:\n{diff_hunk}")
])

# Agent 2: Groq
performance_prompt = ChatPromptTemplate([
    ("system", "You are Agent 2: Systems & Complexity Critic. Scan the git diff ONLY for performance issues "
               "(O(N^2) loops, N+1 queries, unindexed looks, blocking sync calls, memory leaks). "
               "Specify exact line numbers and an optimized fix. If clean, output 'NO_ISSUES'."),
    ("human", "File: {file_path}\nDiff:\n{diff_hunk}")
])

# Agent 3: Gemini
logic_prompt = ChatPromptTemplate([
    ("system", "You are Agent 3: Cross-File Logic Critic. Use the retrieved repository context "
               "and the diff to identify broken function contracts, unhandled null/undefined values, "
               "and edge-case bugs. If clean, output 'NO_ISSUES'."),
    ("human", "Retrieved Repo Context:\n{repo_context}\n\nFile: {file_path}\nDiff:\n{diff_hunk}")
])

# Agent 4: Gemini
synthesizer_prompt = ChatPromptTemplate([
    ("system", "You are Agent 4: Chief Staff Engineer. You receive findings from 3 specialist agents "
               "(Security, Performance, Logic). Deduplicate overlapping comments, drop weak nitpicks, "
               "and return only verified, high-impact suggestions conforming to the requested schema."),
    ("human", "File: {file_path}\nOriginal Diff:\n{diff_hunk}\n\n"
              "--- Security Report ---\n{security_report}\n\n"
              "--- Performance Report ---\n{performance_report}\n\n"
              "--- Logic Report ---\n{logic_report}")
])