import os
from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# AI SIMULATION FUNCTION
# -----------------------------
def analyze_image(image_path, scenario):

    if scenario == "materials":
        return """
==============================
MATERIAL IDENTIFICATION REPORT
==============================

1. Reinforced Concrete:
   - Observed in columns and slabs.
   - Used as primary structural material.
   - Provides compressive strength to the building frame.

2. Steel Reinforcement (Rebar):
   - Embedded inside concrete members.
   - Provides tensile strength.
   - Located in beams, columns, and slabs.

3. Brick Masonry:
   - Used for partition and external walls.
   - Non-load bearing elements.

4. Scaffolding System:
   - Temporary steel support structure.
   - Used for worker access and construction safety.

General Observation:
The structure appears to follow a conventional RCC framed construction system.
"""

    elif scenario == "documentation":
        return """
================================
PROJECT PROGRESS DOCUMENTATION
================================

Completed Work:
- Ground floor slab completed.
- RCC columns constructed up to first floor.
- Partial brick masonry work finished.

Ongoing Work:
- Reinforcement tying for upper slab.
- Formwork installation in progress.
- Scaffolding adjustments ongoing.

Construction Method Observed:
- Cast-in-situ reinforced concrete technique.
- Manual masonry construction.
- Standard steel scaffolding system.

Planned Next Phases:
- Upper floor slab casting.
- Electrical conduit installation.
- Plumbing pipeline routing.
- Exterior plastering work.

Overall Status:
Project appears to be progressing systematically as per standard construction practices.
"""

    elif scenario == "bridge":
        return """
================================
BRIDGE STRUCTURAL ANALYSIS REPORT
================================

Structural Components Identified:

1. Main Beams / Girders:
   - Steel or reinforced concrete beams.
   - Responsible for carrying deck loads.
   - Designed for bending and shear resistance.

2. Columns / Piers:
   - Reinforced concrete vertical supports.
   - Transfer superstructure loads to foundation.

3. Truss Members:
   - Triangular steel framework system.
   - Provides structural stability and load distribution.

4. Deck Slab:
   - Concrete roadway slab supported by beams.
   - Designed for vehicular load transfer.

Materials Used:
- Structural Steel
- Reinforced Concrete

Engineering Observations:
- Proper load distribution mechanism observed.
- Structure appears stable.
- Regular maintenance required to prevent corrosion in steel components.
"""

    else:
        return "Invalid scenario selected."


# -----------------------------
# MAIN ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        try:
            scenario = request.form["scenario"]
            image = request.files["image"]

            if image:
                image_path = "uploaded_image.jpg"
                image.save(image_path)

                result = analyze_image(image_path, scenario)
            else:
                result = "Please upload an image."

        except Exception as e:
            result = f"An error occurred: {str(e)}"

    return render_template("index.html", result=result)


# -----------------------------
# RUN APPLICATION
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)