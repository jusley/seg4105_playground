# Chapter 2: Principles of Shaping

The "Principles of Shaping" describe a method for effectively planning and defining project work. Shaping involves finding the right balance between being too vague and too detailed in project descriptions.

## Key Principles

1. **Avoid Extremes**: Shaping work should not be overly vague or overly detailed. Being too specific too early can stifle creativity and lead to estimation errors, while being too vague makes it hard to understand what the project entails.

2. **Case Study: Dot Grid Calendar**: An example illustrates how to shape a project effectively. Basecamp needed to add a calendar feature but had limited time. They focused on a simplified, two-month grid view called the Dot Grid.

3. **Key Properties of Shaped Work**:
   - *Roughness*: Shaped work is unfinished and leaves room for interpretation by designers and developers.
   - *Solved*: Despite being rough, it presents a clear, thought-through solution.
   - *Bounded*: Shaped work sets limits and defines what not to do, preventing scope creep.

4. **Who Shapes**: Shaping is a creative and integrative process primarily done by designers but requires technical literacy and a strategic mindset. Collaboration with others is also essential.

5. **Two Tracks**: Shaping and building are separate tracks. Shaping happens privately and is not shared until it's ready to be committed to.

6. **Steps to Shaping**:
   - *Set Boundaries*: Determine project scope and constraints.
   - *Rough Out Elements*: Creatively sketch a solution at a higher level of abstraction.
   - *Address Risks and Rabbit Holes*: Identify potential issues and refine the solution.
   - *Write the Pitch*: Create a formal document summarizing the problem, solution, constraints, and risks. This is presented for consideration and, if approved, used at project kick-off.

In essence, shaping is about finding the right level of detail for a project idea, ensuring it's clear and feasible while leaving room for creativity and adaptation. It's a crucial step in effective project planning and execution.

# Chapter 3: Set Boundaries

In the shaping process, the first step is setting boundaries for the project. These boundaries help ensure that discussions are productive and that everyone understands the scope of the project.

## Setting the Appetite

Before diving into a project idea, it's essential to determine how much time and attention it deserves. This is known as setting the "appetite." Some ideas are exciting and may seem worth pursuing immediately, while others may feel like challenges that need addressing.

The appetite is defined based on the project's significance:
- **Small Batch**: Suitable for a team of one designer and one or two programmers, achievable in one or two weeks.
- **Big Batch**: Requires a full six-week effort by the same-sized team.

The appetite is not the same as an estimate. It's a creative constraint that guides the design process, ensuring that the project is scoped appropriately.

## Fixed Time, Variable Scope

The principle of "fixed time, variable scope" is crucial in shaping and shipping projects. It means that having a deadline forces decisions and trade-offs. Without a time constraint, there's always the temptation to add more or improve endlessly. By fixing the time and adapting the scope, projects can be successfully defined and completed.

## "Good" is Relative

The definition of a "good" solution depends on constraints and context. Without a time limit, there's always room for improvement. However, when time is limited, decisions need to be made, and trade-offs are necessary. The context of the project, its time frame, and its importance determine what is considered a "good" solution.

## Responding to Raw Ideas

The default response to new ideas should be cautious and open-ended. Instead of immediately committing to or rejecting an idea, it's important to give it space for evaluation and understanding. Premature commitments can lead to a backlog of work that may not be well-understood.

## Narrowing Down the Problem

In addition to setting the appetite, it's often necessary to narrow down the problem's definition. This involves digging deeper to understand the root of the issue and identify specific pain points or use cases. Narrowing down the problem is essential for shaping a focused solution.

## Watch out for Grab-Bags

Unclear project ideas, such as broad "redesigns" or "refactorings," can be problematic. They often lack a specific problem or use case, making it challenging to define the scope and boundaries. It's more productive to focus on specific problems or challenges within a feature.

With a raw idea, a defined appetite, and a narrowed-down problem definition, the project is ready to move forward to the next step, where the elements of a solution will be defined.

# Chapter 4: Find the Elements

In this chapter, the focus shifts to translating project constraints and problem definitions into concrete elements of a software solution.

## Move at the Right Speed

To effectively find the elements of a solution, two critical factors come into play: having the right people involved and avoiding unnecessary levels of detail in the initial sketches. Collaboration with a trusted partner who can match the pace of idea generation is essential. Starting with wireframes or specific visual layouts is discouraged as it can stifle creativity and exploration.

## Breadboarding

Breadboarding is a prototyping technique borrowed from electrical engineering, allowing design at the right level of abstraction. Three basic elements are used:
1. Places: Navigational elements like screens or menus.
2. Affordances: User-actionable elements like buttons and fields.
3. Connection lines: Indicate how affordances lead from one place to another.

This lightweight notation focuses on components and connections, encouraging discussions and debates on the solution's sequence of actions.

## Fat Marker Sketches

When the solution is primarily visual, fat marker sketches come into play. These sketches are made with broad strokes, making it challenging to add fine detail. They help explore 2D arrangements of elements without getting bogged down in specifics.

## Elements Are the Output

The goal is to identify the essential elements of the solution. For example, in an invoicing tool, this could involve defining a "use this to Autopay" checkbox on the payment screen or a "disable Autopay" option on the invoicer's side.

## Room for Designers

Working at the right "level of abstraction" leaves room for designers to contribute in later stages. By avoiding overly detailed mockups, the shaping process allows for creativity and flexibility in design decisions.

## Not Deliverable Yet

At this stage, the artifacts may be indecipherable to outsiders. The focus is on defining the approach to solving the problem and uncovering concrete elements. Stress-testing and de-risking follow to ensure project viability.

## No Conveyor Belt

It's important to note that, at this stage, there is no commitment to the project. The goal is to make the project more actionable and gather information for potential resource allocation in the future.

This phase of shaping sets the stage for further refinement and development, moving closer to a defined project concept ready for pitching.

# Chapter 5: Risks and Rabbit Holes

In this chapter, the focus is on identifying and mitigating risks associated with a project during the shaping process. The goal is to ensure that the shaped project is as free of holes and uncertainties as possible.

## The Importance of Risk Mitigation

Projects are shaped within a fixed time window, and it's crucial to assess the potential risks that could derail the project. Unforeseen problems can consume a significant portion of the budget, jeopardizing the project's success. Identifying and addressing these risks in advance is essential to ensure smooth execution.

## Different Categories of Risk

Well-shaped projects should resemble a thin-tailed probability distribution in terms of risk. While slight delays may occur, the defined elements should be familiar enough that extended delays are unlikely. Risks, especially rabbit holes such as technical unknowns or design challenges, should be minimized to maintain a thin-tailed probability distribution.

## Look for Rabbit Holes

After sketching out the solution's elements, it's important to slow down and critically examine the concept. This involves analyzing the solution by walking through a use case in slow motion and questioning the viability of each part. Any gaps, technical assumptions, or unsolved design problems should be addressed to prevent passing them onto the project team.

## Case Study: Patching a Hole

An example illustrates the importance of addressing potential holes in the concept. In the To-Do Groups project, the team identified a gap related to displaying completed items. Rather than leaving it as an open design problem, they made a clear decision to dictate a solution in the shaped concept, removing uncertainty and risk from the project.

## Declare Out of Bounds

To keep the project well within the defined appetite, it's advisable to explicitly call out any use cases or features that won't be supported in the project. This ensures that the team focuses on the core value of the project and doesn't get sidetracked by unnecessary additions.

## Cut Back

Sometimes, elements that seemed exciting during the sketching phase may not be necessary for the core project. These should be flagged as nice-to-have but not essential to the project's success. This helps maintain a manageable scope.

## Present to Technical Experts

Before sharing the shaped concept more widely, it's a good practice to involve technical experts to validate assumptions and identify potential risks related to code, design, or user behavior. The goal is to uncover any time bombs that could disrupt the project once it's underway.

## De-risked and Ready to Write Up

At the end of this stage, the shaped project should be free of holes and uncertainties. It's now ready to transition from the private shaping phase to a more public presentation. This involves writing up the concept in a way that communicates the boundaries and the solution for evaluation, resource allocation, and further feedback.

The shaped project should be a solid idea, well-prepared for the next stages of development and execution.
