# CVSS-Score
Free CVSS Score Generator 

The Common Vulnerability Scoring System (CVSS) is a standardized framework that quantifies the severity of security vulnerabilities in information systems on a scale from 0 to 10, where 0 means no severity and 10 represents the most critical threats. This scoring helps organizations prioritize vulnerabilities for remediation based on their potential impact

# How CVSS Score is Calculated
CVSS score is derived from three metric groups:

 -Base Metrics (mandatory):

Represent the intrinsic characteristics of a vulnerability that do not change over time.

Includes two main categories:

Exploitability: Attack Vector, Attack Complexity, Privileges Required, User Interaction.

Impact: Confidentiality Impact, Integrity Impact, Availability Impact.

Also considers the Scope, i.e., whether the vulnerability affects other components beyond the vulnerable one.

The Base score alone is often used for public severity rankings and vulnerability catalogs like NIST’s database.

-Temporal Metrics (optional):

Reflects attributes of a vulnerability that can change over time, such as the availability of patches or the maturity of exploit code.

Includes Exploit Code Maturity, Remediation Level, and Report Confidence.

Modifies the Base score to provide a Temporal score indicating current exploitability and risk.

 -Environmental Metrics (optional):

Allows organizations to adjust the score based on their specific environment, reflecting the business criticality, presence of mitigating controls, and asset use.

Factors such as collateral damage potential, Target Distribution, and the confidentiality, integrity, and availability requirements are taken into account.

<img width="751" height="286" alt="image" src="https://github.com/user-attachments/assets/0a7a917a-680d-42d9-aa32-c1a73a1be2f6" />

# Summary of Key Factors Influencing CVSS Scores
Attack Vector: How remotely an attack can be performed (Network attacks score higher than physical access).

 *Attack Complexity: Ease of conducting an attack, with simpler attacks scoring higher.

 *Privileges Required: Level of access needed prior to exploitation.

 *User Interaction: Whether exploitation requires user involvement.

 *Impact on Confidentiality, Integrity, Availability: The potential damage to these security attributes.

 *Scope: Whether the attack affects a single component or can propagate to others.

 # CVSS Score Calculator

 This is Free tool to calculate the CVSS Score built using Python

 Using This Tool Anyone can Calculate The CVSS Score By Providing Attack Vector(AV), Attack Complexity(AC), Priviledges Required(PR), User Interaction(UI), Scope(S), Confidentiality(C), Intergrity(I), Availability(A) Values as Input

 <img width="538" height="719" alt="image" src="https://github.com/user-attachments/assets/c2b4b003-266b-4762-97d4-780398850bfc" />

 
https://github.com/user-attachments/assets/83d6a0c5-398f-49bd-82cf-f755b715932a


