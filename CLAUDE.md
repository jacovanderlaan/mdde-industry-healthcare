# MDDE Industry: Healthcare

Data models for hospitals, clinics, and healthcare providers with HIPAA/FHIR compliance.

## Purpose

Provides healthcare industry accelerators:
- Hospital operations models
- FHIR R4 resource mappings
- HIPAA compliance patterns
- Clinical and administrative entities

## Structure

```
mdde-industry-healthcare/
├── demos/
│   └── hospital/        # Hospital operations demo
├── fhir_healthcare/     # FHIR R4 resources
├── openemr_healthcare/  # OpenEMR system schema
├── reference/
│   └── cdm_emr/         # EMR CDM standard
```

## Models

| Model | Description | Entities |
|-------|-------------|----------|
| hospital | Hospital operations | 20+ |
| fhir | FHIR R4 HL7 Standard | 50 |
| openemr | OpenEMR System Schema | 21 |
| cdm_emr | EMR CDM standard | 15 |

## FHIR R4 Resources (50)

### Administrative (12)
- Patient, Practitioner, Organization, Location
- Encounter, EpisodeOfCare, Appointment, Schedule

### Clinical (18)
- Condition, Procedure, Observation, DiagnosticReport
- MedicationRequest, MedicationAdministration, Immunization

### Financial (10)
- Coverage, Claim, ClaimResponse, ExplanationOfBenefit

### Foundation (10)
- Bundle, CapabilityStatement, CodeSystem, ValueSet

## Key Metrics

| Metric | Description |
|--------|-------------|
| ALOS | Average Length of Stay |
| Readmission Rate | 30-day readmission % |
| ED Wait Time | Emergency dept wait |
| Bed Occupancy | Utilization rate |

## Compliance

| Standard | Description |
|----------|-------------|
| HIPAA | PHI protection, access controls |
| FHIR | HL7 data exchange |
| ICD-10 | Diagnosis coding |
| CPT | Procedure coding |

## Part of MDDE Industry Accelerators

| Repository | Description |
|------------|-------------|
| mdde | Core framework |
| mdde-industry-healthcare | Healthcare (this repo) |
| mdde-industry-financial | Financial services |
| mdde-industry-retail | Retail |
| mdde-industry-education | Education |
