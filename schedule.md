# Thesis Schedule

This is a living document for my thesis deadlines and schedule. Current details are below.

| Date       | Task                                      | Status   |
|------------|-------------------------------------------|----------|
| 10/06/2025 | Finalize thesis abstract                  | Pending  |

# Notes:

## General Notes:
- Focus on literature review of reverse engineering incorporation into model based systems engineering.
- Consider case studies for practical application (make sure they aren't too complex).
- Current thesis topic: "Bottoms-up: A SysML Approach to Reverse Engineering Cyber-Physical Systems".

## 10/04/2025:
- There are 3 types of RE: Protocol Reverse Engineering (PRE), Hardware Reverse Engineering (HRE), Software Reverse Engineering (SRE).
- There are 3 types of RE approaches: Black Box, Gray Box, White Box.

| Principle                                  | How I Apply It                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| **Use only standard SysML**                | BDD, IBD, Activity, Requirement, Sequence Diagrams.                      |
| **Use minimal relationships**              | `trace`, `refine`, `deriveReqt`, `verify`.                               |
| **Capture evidence simply**                | Comments with file names or addresses.                                   |
| **Show bidirectional linkage**             | Each observation traces *up* to a requirement and *down* to an artifact. |

### Proposed Thesis Structure:
1. Abstract
2. Acknowledgements
3. List of Tables
4. List of Figures
5. Introduction
   - Problem Statement: The increasing complexity of cyber-physical systems necessitates effective reverse engineering techniques to ensure their security and reliability.
   - Research Questions: How can reverse-engineering efforts integrate with SysML to surface unspecified/undesired behavior?
   - Contributions: TODO
6. Case Studies
   - Case Study 1: *White-box* PRE J1708 Protocol and Implementation
   - Case Study 2: *White-box* PRE/SRE/HRE Development of Truck Hacking Platform
   - Case Study 3: *White-box* SRE/PRE Development of CyberEvent IS
   - Case Study 4: *Gray-box* PRE/SRE OneNet Protocol and Implementation
   - Case Study 5: *Gray-box* YDWG-02 MIoT Security Assessment
   - Case Study 6: *Gray-box* ELD Security Assessment
   - Case Study 7: *Black-box* Patching ECM
7. Conclusion
8. Bibliography
  
# Projects to consider incorporating:
- SECURING LEGACY TRANSPORT PROTOCOLS: REQUIREMENTS-DRIVEN MITIGATION FOR COMMUNICATION SYSTEMS (i.e., J1708 protocol vulnerabilities and mitigations):
  - White Box PRE <-> SysML
- Ultimate Truck Hacking Platform (UTHP) (i.e., embedded OS development in conjunction with the NMFTA)
  - White Box SRE/HRE/PRE <-> SysML
- Patching an Engine Control Module to Enhance Security (i.e., testing process for patching an ECU to enhance security)
  - Black Box SRE/PRE/HRE <-> SysML
- VPTP: Vehicle Penetration Testing Platform (i.e., open source vehicle penetration testing platform for automated security testing in the automotive domain)
  - Attempt at automating PRE/HRE/SRE <-> SysML (not sure how to incorporate)
- OneNet Testbench (i.e., creating a testbench for the OneNet protocol by reverse engineering the implementation available)
  - Gray Box PRE/SRE/HRE <-> SysML
- CyberEvent Information Technology (IT) Asset and Attack Surface Management (i.e., reverse engineering the available assets and how to improve the current state of the system)
  - White Box SRE/PRE <-> SysML
- yachtDestroy: A vulnerability exposure tool for recreational marine vessels (i.e., reverse engineering and modeling the System of Interest (SoI) connected to a TCP/IP to NMEA 2000 gateway)
  - Gray Box SRE/PRE/HRE <-> SysML
- FMSCA ELD Mandate (i.e., reverse engineering and modeling the SoI, an ELD device, to understand vulnerabilities and potential mitigations)
  - Gray Box SRE/PRE/HRE <-> SysML
