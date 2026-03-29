# Microsoft CDM - Healthcare Accelerator Mappings

This reference maps MDDE healthcare entities to the Microsoft Common Data Model Healthcare Accelerator for Dynamics 365 and Power Platform integration.

## CDM Entity Mappings

### Patient Domain
| CDM Entity | MDDE Entity | FHIR Resource |
|------------|-------------|---------------|
| `msemr_patient` | `patient` | Patient |
| `msemr_contact` | `contact` | RelatedPerson |
| `msemr_location` | `location` | Location |

### Clinical Domain
| CDM Entity | MDDE Entity | FHIR Resource |
|------------|-------------|---------------|
| `msemr_encounter` | `encounter` | Encounter |
| `msemr_condition` | `condition` | Condition |
| `msemr_observation` | `observation` | Observation |
| `msemr_procedure` | `procedure` | Procedure |
| `msemr_medicationrequest` | `medication_request` | MedicationRequest |
| `msemr_allergyintolerance` | `allergy` | AllergyIntolerance |

### Provider Domain
| CDM Entity | MDDE Entity | FHIR Resource |
|------------|-------------|---------------|
| `msemr_practitioner` | `practitioner` | Practitioner |
| `msemr_practitionerrole` | `practitioner_role` | PractitionerRole |
| `msemr_organization` | `organization` | Organization |

## Integration Patterns

See `cdm_accelerators` in cross_industry reference for detailed integration patterns.

## Resources
- [Healthcare Accelerator Documentation](https://docs.microsoft.com/en-us/dynamics365/industry/healthcare/)
