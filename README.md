# QA Agent Assignment 1A – Requirements Analyst Agent

---

## Overview

This project implements a Requirements Analyst Agent that analyzes e-commerce user stories and extracts structured, testable requirements.

The agent acts as a Senior Business Analyst with strong E-commerce domain expertise and converts natural language business requirements into a machine-readable JSON format.

This agent serves as the foundation for a two-agent system, where Assignment 1B will consume this output to generate detailed test cases.

---

## Assignment Objectives

The agent is designed to:
- Parse natural language user stories
- Extract functional requirements
- Extract non-functional requirements (performance, reliability, security)
- Identify edge cases and boundary conditions
- Detect gaps, ambiguities, and missing requirements
- Assign priority and test complexity
- Generate structured JSON output
- Handle invalid or missing inputs gracefully

---

## Agent Role & Responsibilities

Role:
Requirements Analyst Agent (Senior Business Analyst – E-commerce Domain)

Responsibilities:
- Analyze business user stories
- Identify core functionality and business rules
- Extract testable functional and non-functional requirements
- Highlight validation rules and constraints
- Identify edge cases and boundary conditions
- Perform gap analysis
- Produce structured output for downstream automation

---

## Architecture Overview

```text
project/
├── agent.py              # Core requirement analysis logic
├── main.py               # Entry point to execute the agent
├── sample_input.json     # Sample input containing the user story
├── sample_output.json    # Generated structured requirements output
└── README.md             # Project documentation
```
The user story is read from sample_input.json by main.py. <br>
agent.py analyzes the user story and extracts structured requirements.<br>
The generated output is written to sample_output.json.<br>

---

## Technology Stack

- Programming Language: Python 3.9+
- Architecture: Rule-based Requirements Analyst Agent
- Input Format: JSON
- Output Format: JSON
- External Libraries: None required

---

## Input Specification

The agent accepts a user story in JSON format.

Example (sample_input.json):

```json
{
  "user_story": "As a customer, I want to add products to my shopping cart and modify quantities, so that I can purchase multiple items in a single order."
}


---

## Output Specification

The agent generates structured JSON output containing:
- user_story
- functional_requirements
- non_functional_requirements
- edge_cases
- gaps_identified

Each requirement includes:
- Unique ID
- Clear and testable description
- Priority
- Test complexity
- Category
- Source / traceability

The output is written to sample_output.json.

---

## Error Handling & Validation

The agent validates input before processing.

If the input is missing or invalid, the agent returns:

```json
{
  "error": "Invalid or missing user story input. Please provide a valid user story text."
}



## Usage Guide

To execute the Requirements Analyst Agent:

1. Open a terminal or command prompt in the project directory
2. Run the following command:

   ```bash
   python main.py ```


### Example: Missing or Invalid Input
Input:
```json
{
  "story": "Missing correct key"
}
```

## Integration Notes

The structured JSON output produced by this agent is designed for direct consumption by the **Test Case Designer Agent** in Assignment 1B.

- Each requirement includes a unique ID, category, and traceability information.
- This ensures automated test case generation can reference requirements directly.
- The Traceability Matrix provides linkage between acceptance criteria, requirements, and test cases, enabling downstream validation.

##  Requirement Prioritization Logic

The agent includes a simple prioritization mechanism:
- **High Priority**: Core functionality and business rules critical to checkout flow
- **Medium Priority**: User feedback and validation rules
- **Low Priority**: Optional enhancements or usability features

This prioritization helps stakeholders focus on critical requirements first and guides downstream test case design.



## Traceability Matrix

| Requirement ID | Acceptance Criteria | Test Case Reference | Notes |
|----------------|---------------------|---------------------|-------|
| FR001 | User can add products to cart from product detail page | TC001: Verify add‑to‑cart functionality | Core functionality |
| FR002 | User can update item quantities in the cart | TC002: Verify quantity update | Core functionality |
| FR003 | User can remove items from the cart | TC003: Verify remove‑from‑cart | Core functionality |
| FR004 | Cart displays total price including tax | TC004: Verify price calculation | Pricing & calculation |
| FR005 | Maximum 10 items of any single product allowed | TC005: Verify quantity limit enforcement | Business rule |
| FR006 | Out‑of‑stock items cannot be added to cart | TC006: Verify stock validation | Validation rule |
| FR007 | Cart shows item availability status | TC007: Verify availability display | User feedback |
| FR008 | User receives confirmation when items are added/removed | TC008: Verify confirmation messages | User feedback |
| FR009 | Prevent zero or negative quantity input | TC009: Verify invalid quantity handling | Validation rule |
| FR010 | Cart total recalculates dynamically when quantities change | TC010: Verify dynamic recalculation | Pricing behavior |
| NFR001 | Cart persists during the user session | TC011: Verify session persistence | Reliability |
| NFR002 | Cart operations complete within 2 seconds | TC012: Verify performance under normal load | Performance |
| NFR003 | Cart not accessible to unauthenticated users | TC013: Verify authentication enforcement | Security |
| EC001 | Quantity exceeds limit of 10 | TC014: Verify over‑limit handling | Edge case |
| EC002 | Inventory count is zero | TC015: Verify out‑of‑stock handling | Edge case |
| EC003 | Invalid quantity input (zero/negative) | TC016: Verify invalid input rejection | Edge case |
| EC004 | Session timeout with items in cart | TC017: Verify cart behavior on session expiry | Edge case |
| Gap 1 | Authentication requirements not specified | TC018: Clarify login/cart linkage | Gap for clarification |
| Gap 2 | Tax calculation rules not defined | TC019: Clarify tax rules (region, rounding) | Gap for clarification |
| Gap 3 | Error handling for cart failures unclear | TC020: Clarify error handling | Gap for clarification |
| Gap 4 | Cross‑session/cart persistence not defined | TC021: Clarify persistence across devices | Gap for clarification |

---

## Known Limitations & Future Improvements

- Rule-based keyword analysis is used instead of advanced NLP.
- AI frameworks such as CrewAI or LangChain can be integrated in future.
- Only single user story input is supported currently.
- No real-time integration with inventory, pricing, or authentication systems.
- Error handling can be extended for downstream service failures.

---

## Conclusion

This Requirements Analyst Agent fulfills all success criteria defined in QA Agent Assignment 1A.

It demonstrates structured requirement extraction, test-ready outputs, robust validation, and clear documentation.

Status: Submission Ready 
