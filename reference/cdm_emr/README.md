# Healthcare CDM - EMR/EHR Reference Model

This reference model provides standardized entities for Electronic Medical/Health Record systems, aligned with FHIR R4 and HL7 standards.

## Overview

The EMR CDM covers clinical, administrative, and financial healthcare data domains commonly found in hospital information systems and electronic health records.

## Domain Areas

### Clinical Domain
| Entity | FHIR Resource | Description |
|--------|---------------|-------------|
| `patient` | Patient | Patient demographics |
| `encounter` | Encounter | Patient visits/encounters |
| `condition` | Condition | Diagnoses/problems |
| `observation` | Observation | Clinical observations |
| `procedure` | Procedure | Clinical procedures |
| `medication_request` | MedicationRequest | Prescriptions |
| `diagnostic_report` | DiagnosticReport | Lab/imaging reports |
| `allergy_intolerance` | AllergyIntolerance | Allergies |

### Administrative Domain
| Entity | FHIR Resource | Description |
|--------|---------------|-------------|
| `practitioner` | Practitioner | Healthcare providers |
| `organization` | Organization | Healthcare facilities |
| `location` | Location | Care locations |
| `schedule` | Schedule | Appointment schedules |
| `appointment` | Appointment | Scheduled visits |

### Financial Domain
| Entity | FHIR Resource | Description |
|--------|---------------|-------------|
| `claim` | Claim | Insurance claims |
| `coverage` | Coverage | Insurance coverage |
| `account` | Account | Patient accounts |

## Standards Alignment

- **FHIR R4**: HL7 FHIR Release 4
- **HL7 v2.x**: Legacy message segments
- **ICD-10**: Diagnosis codes
- **CPT/HCPCS**: Procedure codes
- **LOINC**: Lab/observation codes
- **SNOMED CT**: Clinical terminology
- **RxNorm**: Medication codes
