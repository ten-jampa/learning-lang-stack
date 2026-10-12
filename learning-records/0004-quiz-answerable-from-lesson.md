# Every quiz question must be answerable from the lesson's own materials

User's bar: a quiz is only fair if its questions (including why distractors are wrong) can be answered from what the lesson taught. Audit caught a violation in lesson 0001: Q2's "LangSmith dashboard" distractor referenced a tool the lesson never introduced, and Q1's contrasts (no bundled planning/subagents/filesystem in `create_agent`; hand-built wiring in `StateGraph`) were implied, not stated.

Evidence: user feedback 2026-10-12; fixed by stating limits explicitly + one-line LangSmith framing in section 1.
Implications: before shipping any lesson, trace each quiz option back to a specific taught sentence; if an option needs knowledge from outside the lesson, either teach it or drop the option.
