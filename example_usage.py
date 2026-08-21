from client import ConstructionProjectMaterialTakeoffEstimatorClient

def main():
    client = ConstructionProjectMaterialTakeoffEstimatorClient()
    res = client.estimate_takeoff("2-story residential remodel with open-plan ground floor", 2800.0)
    print(f"Bid Summary: {res['bid_summary']}")
    print(f"Total Material Cost: ${res['total_material_cost_usd']:,}")
    print(f"Labor Estimate: {res['labor_estimate_hours']} hours")
    print("Material Quantities:")
    for m in res["material_quantities"]:
        print(f"  {m['item']}: {m['quantity']} {m['unit']} @ ${m['unit_cost_usd']}/unit = ${m['total_usd']:,}")

if __name__ == "__main__":
    main()
