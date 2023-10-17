
# A Comparison of Partial Information Decompositions Using Data from Real and Simulated Layer 5b Pyramidal Cells

## Partial Information Decomposition (PID) Methods:
- Multiple methods for PID have been introduced, including Imin, Iproj, Ibroja, Idep, Iig, Iprec, among others.
- The first four PIDs guarantee nonnegative components, while Iig, though initially claimed to be nonnegative, has been found to produce negative estimates of redundancy in some cases.
- Pointwise PIDs can produce negative components, termed as "misinformation."

## Importance of PID:
- PID allows for the separate estimation of shared and synergistic information in a system.
- Earlier research used interaction information to estimate synergy, which could be negative, and the three-way mutual information or coinformation, which also could be negative.

## Notation and Definitions:
- The article focuses on trivariate probabilistic systems involving an output \( Y \) and two inputs \( B \) and \( A \).
- Several standard information theoretic terms are defined, including Shannon entropy and joint mutual information.
- Formulas provided for calculating:
  - Joint mutual information shared by \( Y \) and the pair \( (B, A) \)
  - Information shared between \( Y \) and \( B \) or \( A \), considering the influence of the other input.
  - Interaction information and coinformation involving all three variables \( Y \), \( B \), and \( A \).

## Partial Information Decomposition (PID):
- The article delves into the intricacies of PID, discussing the various measures and methods to compute the decomposition.
- The significance of understanding the decomposition in the context of neural data is emphasized.
