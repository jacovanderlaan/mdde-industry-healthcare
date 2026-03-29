#!/usr/bin/env python3
"""
Healthcare Demo Script.

Demonstrates MDDE capabilities for healthcare data modeling including
FHIR R4 mapping, HL7 processing, and HIPAA compliance.
"""

import sys
import yaml
from pathlib import Path

# Add MDDE to path
sys.path.insert(0, str(Path(__file__).parents[4] / "src"))


def main():
    print("=" * 70)
    print("MDDE Healthcare Demo (FHIR R4 / HIPAA)")
    print("=" * 70)

    demo_dir = Path(__file__).parent.parent
    entities_dir = demo_dir / "entities"

    # Parse model
    print("\n1. Parsing Healthcare Model...")

    entities = []
    for layer in ["source", "staging", "integration", "business"]:
        layer_dir = entities_dir / layer
        if layer_dir.exists():
            for yaml_file in layer_dir.glob("*.yaml"):
                try:
                    with open(yaml_file, "r", encoding="utf-8") as f:
                        entity = yaml.safe_load(f)
                    entities.append(entity)
                    print(f"   Parsed: {entity.get('entity', {}).get('entity_id', yaml_file.stem)}")
                except Exception as e:
                    print(f"   Error parsing {yaml_file.name}: {e}")

    print(f"\n   Total entities: {len(entities)}")

    # Analyze by layer
    print("\n2. Entity Distribution by Layer...")
    layers = {}
    for entity in entities:
        layer = entity.get("entity", {}).get("layer", "unknown")
        layers[layer] = layers.get(layer, 0) + 1

    for layer, count in sorted(layers.items()):
        print(f"   {layer}: {count} entities")

    # Find PHI attributes
    print("\n3. PHI-Tagged Attributes (HIPAA)...")
    phi_count = 0
    for entity in entities:
        entity_data = entity.get("entity", {})
        entity_id = entity_data.get("entity_id", "unknown")
        for attr in entity_data.get("attributes", []):
            tags = attr.get("tags", [])
            if "phi" in tags:
                phi_count += 1
                if phi_count <= 15:
                    print(f"   {entity_id}.{attr['name']}")

    if phi_count > 15:
        print(f"   ... and {phi_count - 15} more")
    print(f"\n   Total PHI attributes: {phi_count}")

    # Find FHIR mappings
    print("\n4. FHIR R4 Mappings...")
    fhir_count = 0
    for entity in entities:
        entity_data = entity.get("entity", {})
        entity_id = entity_data.get("entity_id", "unknown")
        fhir_mapping = entity_data.get("fhir_mapping", {})
        if fhir_mapping:
            resource = fhir_mapping.get("resource", fhir_mapping.get("resources", []))
            print(f"   {entity_id} -> {resource}")
            fhir_count += 1

    print(f"\n   Entities with FHIR mappings: {fhir_count}")

    # Find HL7 mappings
    print("\n5. HL7 Segment Mappings...")
    hl7_attrs = 0
    for entity in entities:
        entity_data = entity.get("entity", {})
        for attr in entity_data.get("attributes", []):
            if attr.get("hl7_segment"):
                hl7_attrs += 1

    print(f"   Attributes with HL7 mappings: {hl7_attrs}")

    # HIPAA compliance
    print("\n6. HIPAA Compliance Coverage...")
    hipaa_entities = []
    for entity in entities:
        entity_data = entity.get("entity", {})
        entity_id = entity_data.get("entity_id", "unknown")
        compliance = entity_data.get("compliance", {})
        hipaa = compliance.get("hipaa", {})
        if hipaa.get("scope"):
            hipaa_entities.append(entity_id)
            phi_elements = hipaa.get("phi_elements", [])
            print(f"   {entity_id}: {len(phi_elements)} PHI elements")

    print(f"\n   HIPAA-scoped entities: {len(hipaa_entities)}")

    # Encrypted fields
    print("\n7. Encrypted Fields...")
    encrypted_count = 0
    for entity in entities:
        entity_data = entity.get("entity", {})
        entity_id = entity_data.get("entity_id", "unknown")
        for attr in entity_data.get("attributes", []):
            security = attr.get("security", {})
            if security.get("encrypted"):
                encrypted_count += 1
                key = security.get("encryption_key", "default")
                print(f"   {entity_id}.{attr['name']} (key: {key})")

    print(f"\n   Total encrypted fields: {encrypted_count}")

    # Quality rules
    print("\n8. Quality Rules...")
    total_rules = 0
    for entity in entities:
        entity_data = entity.get("entity", {})
        rules = entity_data.get("quality_rules", [])
        total_rules += len(rules)

    print(f"   Total quality rules: {total_rules}")

    print("\n" + "=" * 70)
    print("Healthcare Demo Complete!")
    print("=" * 70)
    print(f"\nModel Summary:")
    print(f"  - Entities: {len(entities)}")
    print(f"  - PHI Attributes: {phi_count}")
    print(f"  - FHIR Mappings: {fhir_count}")
    print(f"  - HL7 Mappings: {hl7_attrs}")
    print(f"  - Encrypted Fields: {encrypted_count}")
    print(f"  - Quality Rules: {total_rules}")


if __name__ == "__main__":
    main()
