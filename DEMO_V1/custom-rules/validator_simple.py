#!/usr/bin/env python3
"""
AIM Stack - Simple Integrated Validator
This validator applies rules AND saves results to AIM dashboard
"""

import aim
from datetime import datetime

class SimpleAIMValidator:
    """Simplified validator that saves results to AIM"""
    
    def validate_and_save_to_aim(self, target_run_hash):
        """
        Validates an experiment and saves results as new AIM run
        """
        print(f"🔍 Validating experiment {target_run_hash[:8]}...")
        
        # Create new AIM run for validation
        validation_run = aim.Run()
        validation_run.name = f"VALIDATION_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Find original run
        repo = aim.Repo(".")
        target_run = None
        
        for run in repo.iter_runs():
            if run.hash == target_run_hash:
                target_run = run
                break
        
        if not target_run:
            print(f"❌ Run {target_run_hash[:8]} not found!")
            return None
        
        # Extract data from original experiment
        hparams = target_run.get("hparams", {})
        results = target_run.get("results", {})
        
        # Apply simple validations
        errors = []
        warnings = []
        
        # Validation 1: Learning Rate
        lr = hparams.get("learning_rate", 0)
        if lr == 0:
            errors.append("Learning rate not defined")
        elif not (0.0001 <= lr <= 0.1):
            errors.append(f"Learning rate {lr} outside recommended range [0.0001, 0.1]")
        else:
            validation_run.track(1.0, name="lr_valid", step=0)
            
        # Validation 2: Epochs
        epochs = hparams.get("epochs", 0)
        if epochs < 10:
            warnings.append(f"Number of epochs ({epochs}) is low, consider increasing")
        validation_run.track(epochs, name="epochs_count", step=0)
        
        # Validation 3: Final accuracy
        final_acc = results.get("final_accuracy", 0)
        if final_acc < 0.5:
            warnings.append(f"Final accuracy ({final_acc:.3f}) could be improved")
        validation_run.track(final_acc, name="final_accuracy", step=0)
        
        # Validation 4: Naming convention
        if not target_run.name or len(target_run.name) < 5:
            warnings.append("Experiment name too short")
        
        # Calculate quality score
        quality_score = 100
        quality_score -= len(errors) * 20  # -20 points per error
        quality_score -= len(warnings) * 10  # -10 points per warning
        quality_score = max(0, quality_score)
        
        # Save validation results
        is_valid = len(errors) == 0
        
        validation_run["validation_metadata"] = {
            "target_run_hash": target_run_hash,
            "target_run_name": target_run.name,
            "timestamp": datetime.now().isoformat(),
            "total_errors": len(errors),
            "total_warnings": len(warnings),
            "quality_score": quality_score,
            "status": "PASS" if is_valid else "FAIL"
        }
        
        validation_run["validation_details"] = {
            "errors": errors,
            "warnings": warnings,
            "validated_params": {
                "learning_rate": lr,
                "epochs": epochs,
                "final_accuracy": final_acc,
                "run_name": target_run.name
            }
        }
        
        # Track metrics for charts
        validation_run.track(1.0 if is_valid else 0.0, name="validation_success", step=0)
        validation_run.track(len(errors), name="error_count", step=0)
        validation_run.track(len(warnings), name="warning_count", step=0)
        validation_run.track(quality_score, name="quality_score", step=0)
        
        # Add tags for filtering
        validation_run.add_tag("validation")
        validation_run.add_tag("PASS" if is_valid else "FAIL")
        validation_run.add_tag(f"target_{target_run_hash[:8]}")
        
        # Display results
        status = "✅ PASS" if is_valid else "❌ FAIL"
        print(f"Status: {status} (Quality Score: {quality_score}/100)")
        
        if errors:
            print(f"🚨 Errors ({len(errors)}):")
            for error in errors:
                print(f"   • {error}")
        
        if warnings:
            print(f"⚠️  Warnings ({len(warnings)}):")
            for warning in warnings:
                print(f"   • {warning}")
        
        print(f"✅ Validation saved to AIM as run: {validation_run.hash[:8]}")
        return validation_run
    
    def validate_all_experiments(self):
        """Validates all experiments and saves to AIM"""
        
        print("🎯 Validating ALL experiments...")
        print("=" * 50)
        
        repo = aim.Repo(".")
        validation_count = 0
        
        for run in repo.iter_runs():
            # Skip validation runs
            if run.name and "VALIDATION_" in run.name:
                continue
            
            print(f"\n📊 Experiment: {run.name} ({run.hash[:8]})")
            self.validate_and_save_to_aim(run.hash)
            validation_count += 1
            print("-" * 30)
        
        print("=" * 50)
        print(f"✅ {validation_count} experiments validated!")
        print("🌐 View in AIM dashboard: http://localhost:43800")
        print("💡 Filter by 'validation' tag to see validations")

def main():
    """Integrated validator demonstration"""
    
    print("🎯 AIM Stack - Validator Integrated to Dashboard")
    print("=" * 60)
    
    validator = SimpleAIMValidator()
    
    # Validate all experiments
    validator.validate_all_experiments()
    
    print("\n" + "=" * 60)
    print("✅ Integrated validation completed!")
    print("\n🌐 NOW IN AIM DASHBOARD YOU'LL SEE:")
    print("   📊 Validation runs with visual metrics")
    print("   🏷️  Tags for filtering (validation, PASS/FAIL)")
    print("   📈 Charts for quality_score, error_count, etc.")
    print("   🔍 Complete details in metadata")
    print("\n💡 HOW TO USE IN DASHBOARD:")
    print("   1. Open: aim up")
    print("   2. Filter by tag: 'validation'")
    print("   3. Compare quality_score between experiments")
    print("   4. View error/warning details")
    print("   5. Use charts to identify patterns")

if __name__ == "__main__":
    main()
