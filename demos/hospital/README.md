# Healthcare Demo (FHIR R4 / HL7 / HIPAA)

This demo showcases MDDE capabilities for healthcare data modeling, including:

- **FHIR R4 Mapping**: Direct mapping to FHIR resources (Patient, Encounter, Observation, etc.)
- **HL7 v2.x Integration**: HL7 segment mapping for message processing
- **HIPAA Compliance**: PHI identification, encryption requirements, and access controls
- **Clinical Workflows**: Patient demographics, encounters, diagnoses, procedures, lab results

## Architecture (18 entities)

```
Source Layer (4 entities):
  src_ehr_system         - EHR data via API (Patient, Encounter, Condition)
  src_hl7_messages       - HL7 v2.x message streams (ADT, ORU, ORM)
  src_claims_feed        - Insurance claims (X12 837, FHIR Claim)
  src_lab_results        - Lab results via HL7 ORU (Observation, DiagnosticReport)

Staging Layer (2 entities):
  stg_patients           - Cleaned patient data (FHIR Patient)
  stg_encounters         - Validated encounter data (FHIR Encounter)

Integration Layer - Data Vault (8 entities):
  hub_patient            - Patient hub
  hub_provider           - Provider hub (Practitioner, Organization)
  hub_encounter          - Encounter hub
  sat_patient_demographics - Patient demographics satellite
  sat_provider_details   - Provider details satellite
  sat_encounter_details  - Encounter details satellite
  link_patient_encounter - Patient-Encounter link
  link_encounter_provider - Encounter-Provider link

Business Layer (4 entities):
  dim_patient_hc         - Patient dimension with SCD2
  dim_provider           - Provider dimension with SCD2
  fact_encounter         - Encounter fact table
  fact_clinical_event    - Clinical events (diagnoses, procedures, labs, meds)
```

## Key Features Demonstrated

### FHIR R4 Resource Mapping
- **Patient**: Demographics, identifiers, contact info
- **Encounter**: Visit information, diagnoses, procedures
- **Observation**: Vital signs, lab results
- **MedicationRequest**: Prescriptions, dosing
- **Claim**: Insurance claims processing

### Data Vault Integration Layer
- **Hubs**: Patient, Provider, Encounter, Organization
- **Links**: Patient-Provider relationships, Encounter-Diagnosis
- **Satellites**: Demographics, clinical details, insurance

### HIPAA Compliance
- **PHI Tagging**: All protected health information tagged
- **De-identification**: Safe harbor method support
- **Audit Logging**: Access tracking for all PHI
- **Encryption**: At-rest encryption for sensitive fields

### Healthcare-Specific Tags
- `phi`: Protected Health Information
- `hipaa_covered`: HIPAA-regulated data
- `pii`: Personally Identifiable Information
- `clinical`: Clinical/medical data
- `financial`: Claims/billing data

## Running the Demo

```bash
cd /path/to/mdde
python workspace/demos/healthcare/scripts/run_demo.py
```

## Sample Output

```
MDDE Healthcare Demo (FHIR R4 / HIPAA)
======================================================================

Total entities: 18
PHI Attributes: 61
FHIR Mappings: 17
HL7 Mappings: 25
Encrypted Fields: 7
Quality Rules: 45
```

## Use Cases

1. **Patient 360**: Unified patient view across EHR systems
2. **Clinical Analytics**: Encounter, diagnosis, and procedure analysis
3. **Population Health**: Cohort identification and risk stratification
4. **Revenue Cycle**: Claims processing and denial management
5. **Quality Reporting**: CMS quality measure calculation
