class ConstructionProjectMaterialTakeoffEstimatorClient:
    def estimate_takeoff(self, project_description: str, floor_area_sqft: float = 2400.0) -> dict:
        materials = [
            {"item": "Concrete (slab)", "quantity": round(floor_area_sqft * 0.041, 1), "unit": "cubic yards", "unit_cost_usd": 148, "total_usd": round(floor_area_sqft * 0.041 * 148, 2)},
            {"item": "Lumber (framing)", "quantity": round(floor_area_sqft * 1.6, 0), "unit": "board feet", "unit_cost_usd": 1.15, "total_usd": round(floor_area_sqft * 1.6 * 1.15, 2)},
            {"item": "Drywall", "quantity": round(floor_area_sqft * 2.1, 0), "unit": "sq ft", "unit_cost_usd": 0.58, "total_usd": round(floor_area_sqft * 2.1 * 0.58, 2)},
            {"item": "Roofing shingles", "quantity": round(floor_area_sqft / 100, 1), "unit": "squares", "unit_cost_usd": 320, "total_usd": round(floor_area_sqft / 100 * 320, 2)}
        ]
        total = sum(m["total_usd"] for m in materials)
        return {
            "material_quantities": materials,
            "total_material_cost_usd": round(total, 2),
            "labor_estimate_hours": round(floor_area_sqft * 0.85, 1),
            "bid_summary": f"Project: {project_description} | Area: {floor_area_sqft:,} sqft | Materials: ${total:,.2f} | Labor: {round(floor_area_sqft*0.85,1)}hrs"
        }
