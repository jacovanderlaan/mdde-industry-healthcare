# Healthcare Industry Models

Data models for hospitals, clinics, and healthcare providers with HIPAA/FHIR compliance.

## Available Models

### Demos
| Demo | Description | Entities | Patterns |
|------|-------------|----------|----------|
| **hospital** | Hospital operations | 20+ | Data Vault + Dimensional |

### Reference Models
| Model | Description | Entities |
|-------|-------------|----------|
| **cdm_emr** | Electronic Medical Records CDM | 15 |

### Regulatory Frameworks
| Framework | Description | Resources |
|-----------|-------------|-----------|
| **fhir** | FHIR R4 HL7 Standard | 50 |
| **openemr** | OpenEMR System Schema | 21 |

## Demo: Hospital

Complete hospital operations model:
- **Source**: `src_patient`, `src_encounter`, `src_provider`, `src_procedure`
- **Integration**: Patient hub, encounter satellites, provider links
- **Business**: `dim_patient`, `dim_provider`, `fact_encounter`, `fact_procedure`

### Running the Demo

```bash
python workspace/industries/healthcare/demos/hospital/scripts/run_demo.py
```

## FHIR R4 Resources

50 FHIR R4 resources across 4 categories:

### Administrative (12)
- Patient, Practitioner, Organization, Location
- Encounter, EpisodeOfCare, Appointment, Schedule
- Account, Coverage, Claim, ClaimResponse

### Clinical (18)
- Condition, Procedure, Observation, DiagnosticReport
- MedicationRequest, MedicationAdministration, Immunization
- AllergyIntolerance, CarePlan, ServiceRequest

### Financial (10)
- Coverage, Claim, ClaimResponse, ExplanationOfBenefit
- PaymentReconciliation, Invoice, ChargeItem

### Foundation (10)
- Bundle, CapabilityStatement, OperationOutcome
- CodeSystem, ValueSet, ConceptMap

## Compliance Features

| Standard | Description | Location |
|----------|-------------|----------|
| HIPAA | PHI protection, access controls | Entity tags, encryption markers |
| FHIR | HL7 data exchange | FHIR resource mappings |
| ICD-10 | Diagnosis coding | `diagnosis_code` domain |
| CPT | Procedure coding | `procedure_code` domain |

## Key Metrics

| Metric | Description |
|--------|-------------|
| ALOS | Average Length of Stay |
| Readmission Rate | 30-day readmission % |
| ED Wait Time | Emergency dept wait |
| Bed Occupancy | Utilization rate |
