# AIM Stack Custom Rules - ML Experiment Tracking & Governance

A proof of concept demonstrating **AIM Stack** implementation for ML experiment tracking with custom validation rules and automated governance.

## Overview

This project showcases how to implement **experiment tracking** and **governance** for machine learning workflows using the open-source AIM Stack platform. It includes:

- **Automated experiment tracking** with metrics and hyperparameters
- **Custom validation rules** for experiment governance
- **Interactive web dashboard** for experiment visualization
- **Real-time validation** with quality scoring
- **Technical presentation** materials for demonstrations

## 🛠️ Technology Stack

- **AIM Stack**: Open-source ML experiment tracking platform
- **Python 3.7+**: Core development language
- **HTML/CSS/JavaScript**: Interactive presentation interface
- **Local storage**: Experiments stored in `.aim/` directory

## 📁 Project Structure

```
DEMO_V1/
├── README.md                    # This documentation
├── basic_tracking.py           # Basic AIM tracking demonstration
├── custom-rules/
│   └── validator_simple.py     # Custom validation rules implementation
├── slide.html                  # Interactive presentation slides
```

## 📋 File Descriptions

### Core Implementation Files

#### `basic_tracking.py`
**Purpose**: Demonstrates basic AIM Stack functionality
- Creates ML experiment runs with hyperparameters
- Tracks metrics (accuracy, loss) over time
- Simulates training loops with realistic data
- Shows data persistence in AIM format

**Key Features**:
- Automated experiment naming
- Hyperparameter logging
- Real-time metric tracking
- Multiple experiment scenarios

#### `custom-rules/validator_simple.py`
**Purpose**: Implements custom validation rules for ML governance
- Validates experiment configurations
- Applies business rules and best practices
- Generates quality scores and compliance reports
- Integrates validation results into AIM dashboard

**Validation Rules**:
- Learning rate range validation (0.0001 - 0.1)
- Minimum epochs requirement (≥10)
- Accuracy threshold checks
- Naming convention enforcement
- Quality scoring system (0-100)

### Presentation Materials

#### `slide.html`
**Purpose**: Interactive technical presentation
- 9-slide Lightning Talk format (5 minutes)
- Modern, responsive design
- Built-in timer and navigation
- Live demo integration
- Keyboard shortcuts and fullscreen support

**Features**:
- Tech-focused visual design
- Code examples with syntax highlighting
- Interactive navigation (arrows, touch, keyboard)
- Presentation timer with visual alerts
- Mobile-responsive layout

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/gfnogueira/AIM-custom-rules.git
cd AIM-custom-rules/DEMO_V1
```

2. **Install AIM Stack**
```bash
pip install aim
```

3. **Initialize AIM repository**
```bash
aim init
```

### Running the Demo

#### 1. Basic Experiment Tracking
```bash
python basic_tracking.py
```
**Expected Output**:
- Creates 3 different experiment scenarios
- Tracks metrics and hyperparameters
- Saves data to `.aim/` directory
- Displays experiment summaries

#### 2. Custom Validation Rules
```bash
python custom-rules/validator_simple.py
```
**Expected Output**:
- Validates all existing experiments
- Applies governance rules
- Generates quality scores
- Creates validation runs in AIM

#### 3. Launch AIM Dashboard
```bash
aim up
```
**Result**: Opens web interface at `http://localhost:43800`

#### 4. View Interactive Presentation
Open `slide.html` in your browser for the technical presentation.

## 🎨 AIM Dashboard Features

After running the demo, the AIM dashboard will show:

### Experiment Overview
- **Run list**: All experiments with metadata
- **Metrics visualization**: Interactive charts and graphs
- **Hyperparameter comparison**: Side-by-side analysis
- **Tag filtering**: Easy experiment categorization

### Validation Results
- **Quality scores**: Visual quality metrics (0-100)
- **Compliance status**: PASS/FAIL validation results
- **Error tracking**: Detailed validation errors and warnings
- **Governance metrics**: Rule compliance over time

### Filtering and Search
- Filter by tags: `validation`, `PASS`, `FAIL`
- Search by experiment names
- Date range filtering
- Custom metric filtering

## 🔧 Advanced Usage

### Creating Custom Validation Rules

Extend `validator_simple.py` to add new rules:

```python
# Add to validate_and_save_to_aim method
def validate_custom_rule(self, hparams, results):
    if hparams.get("custom_param") < threshold:
        return "Custom validation failed"
    return None
```

### Adding New Experiments

Use `basic_tracking.py` as template:

```python
import aim

run = aim.Run()
run.name = "my_experiment"
run["hparams"] = {"lr": 0.01, "epochs": 100}
run.track(0.95, name="accuracy", step=1)
```

### Presentation Customization

Modify `slide.html`:
- Update content in slide sections
- Adjust styling in `<style>` section
- Add new slides following existing pattern

## 📊 Use Cases

### 1. ML Experiment Management
- Track multiple model training runs
- Compare hyperparameter configurations
- Monitor training progress in real-time
- Maintain experiment history

### 2. ML Governance & Compliance
- Enforce corporate ML standards
- Validate experiment configurations
- Generate compliance reports
- Audit model development process

### 3. Team Collaboration
- Share experiment results across teams
- Standardize ML development workflows
- Maintain centralized experiment database
- Enable reproducible ML research

### 4. Technical Presentations
- Demonstrate ML tracking capabilities
- Show governance implementation
- Present technical concepts visually
- Conduct live technical demos

## 🔍 Technical Details

### AIM Stack Architecture
- **Local storage**: Experiments stored in `.aim/` directory
- **Web interface**: React-based dashboard on port 43800
- **Python SDK**: Native Python integration for tracking
- **REST API**: Programmatic access to experiment data

### Performance Characteristics
- **Lightweight**: Minimal overhead during training
- **Scalable**: Handles thousands of experiments
- **Fast queries**: Efficient experiment retrieval
- **Real-time**: Live experiment monitoring

### Data Persistence
- **Format**: Optimized binary storage
- **Backup**: Portable `.aim/` directory
- **Version control**: Git-friendly structure
- **Export**: JSON/CSV export capabilities

## 🎓 Learning Outcomes

After completing this demo, you'll understand:

1. **AIM Stack basics**: Installation, initialization, and core concepts
2. **Experiment tracking**: How to log metrics, hyperparameters, and metadata
3. **Custom validation**: Implementing governance rules for ML experiments
4. **Dashboard usage**: Navigating and utilizing the AIM web interface
5. **Integration patterns**: How to embed AIM in existing ML workflows

## 🔗 Additional Resources

- **AIM Stack Documentation**: [https://aimstack.io](https://aimstack.io)
- **GitHub Repository**: [https://github.com/aimhubio/aim](https://github.com/aimhubio/aim)
- **Community**: [AIM Stack Discord](https://discord.gg/GFBZpfkJ)
- **Examples**: [Official AIM Examples](https://github.com/aimhubio/aim/tree/main/examples)

---
