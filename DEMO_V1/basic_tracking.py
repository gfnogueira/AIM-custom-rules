#!/usr/bin/env python3
"""
AIM Stack - Basic Example
Basic ML experiment tracking demonstration
"""

import aim
import math
import random
import time
from datetime import datetime

def basic_experiment():
    """Basic AIM tracking example"""
    
    print("Starting basic AIM Stack experiment...")
    
    # Initialize AIM run
    run = aim.Run()
    
    # Set experiment name
    run.name = f"basic_experiment_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Track hyperparameters
    hparams = {
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 50,
        "model_type": "CNN",
        "optimizer": "Adam",
        "dataset": "CIFAR-10"
    }
    
    run["hparams"] = hparams
    print(f"Hyperparameters logged: {hparams}")
    
    # Simulate training loop
    print("Simulating training...")
    
    for epoch in range(hparams["epochs"]):
        # Simulate realistic training metrics
        
        # Accuracy improves over time with noise
        accuracy = 0.1 + 0.85 * (1 - math.exp(-epoch/15)) + 0.05 * random.random()
        
        # Loss decreases over time with noise  
        loss = 2.5 * math.exp(-epoch/10) + 0.1 * random.random()
        
        # Apply learning rate decay
        current_lr = hparams["learning_rate"] * (0.95 ** (epoch // 10))
        
        # Track metrics
        run.track(accuracy, name='accuracy', epoch=epoch)
        run.track(loss, name='loss', epoch=epoch) 
        run.track(current_lr, name='learning_rate', epoch=epoch)
        
        # Log validation metrics every 10 epochs
        if epoch % 10 == 0:
            val_accuracy = accuracy - 0.05 + 0.02 * random.random()
            val_loss = loss + 0.1 + 0.05 * random.random()
            
            run.track(val_accuracy, name='val_accuracy', epoch=epoch)
            run.track(val_loss, name='val_loss', epoch=epoch)
            
            print(f"Epoch {epoch:2d}: acc={accuracy:.3f}, loss={loss:.3f}, val_acc={val_accuracy:.3f}")
        
        # Simulate training time
        time.sleep(0.05)
    
    # Store final results
    final_results = {
        "final_accuracy": accuracy,
        "final_loss": loss,
        "converged_epoch": epoch,
        "total_params": 1_234_567
    }
    
    run["results"] = final_results
    print(f"✅ Experiment completed! Results: {final_results}")
    
    return run

def advanced_experiment_with_images():
    """Advanced example with image tracking"""
    
    print("🖼️ Starting experiment with images...")
    
    run = aim.Run()
    run.name = "advanced_experiment_with_images"
    
    # Import numpy for image simulation
    import numpy as np
    
    # Track hyperparameters
    run["hparams"] = {
        "model": "GAN",
        "generator_lr": 0.0002, 
        "discriminator_lr": 0.0001,
        "batch_size": 64,
        "noise_dim": 100
    }
    
    for epoch in range(20):
        # Simulate GAN training losses
        gen_loss = 2.0 * math.exp(-epoch/8) + 0.3 * random.random()
        disc_loss = 1.5 + 0.5 * math.sin(epoch/3) + 0.2 * random.random()
        
        run.track(gen_loss, name='generator_loss', epoch=epoch)
        run.track(disc_loss, name='discriminator_loss', epoch=epoch)
        
        # Track generated images every 5 epochs
        if epoch % 5 == 0:
            # Generate fake image data for demo
            fake_image = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
            run.track(aim.Image(fake_image), name='generated_images', epoch=epoch)
            
            print(f"Epoch {epoch}: gen_loss={gen_loss:.3f}, disc_loss={disc_loss:.3f}")
        
        time.sleep(0.1)
    
    print("✅ Image experiment completed!")
    return run

def experiment_with_text():
    """Text experiment example with prompt tracking"""
    
    print("📝 Starting text experiment...")
    
    run = aim.Run()
    run.name = "text_experiment_prompts"
    
    # Define sample prompts for testing
    prompts = [
        "Explain quantum computing in simple terms",
        "Write a creative story about AI", 
        "Summarize the benefits of renewable energy",
        "Create a recipe for chocolate cake"
    ]
    
    run["hparams"] = {
        "model": "GPT-4",
        "temperature": 0.7,
        "max_tokens": 150,
        "top_p": 0.9
    }
    
    for i, prompt in enumerate(prompts):
        # Simulate LLM response quality metrics
        relevance = 0.7 + 0.3 * random.random()
        coherence = 0.6 + 0.4 * random.random() 
        creativity = 0.5 + 0.5 * random.random()
        
        # Track quality metrics
        run.track(relevance, name='relevance', step=i)
        run.track(coherence, name='coherence', step=i)
        run.track(creativity, name='creativity', step=i)
        
        # Track prompts and responses
        run.track(aim.Text(prompt), name='prompts', step=i)
        
        # Simulate response (truncated for demo)
        response = f"Generated response for prompt {i+1}... [truncated]"
        run.track(aim.Text(response), name='responses', step=i)
        
        print(f"Prompt {i+1}: relevance={relevance:.3f}, coherence={coherence:.3f}")
        
        time.sleep(0.2)
    
    print("✅ Text experiment completed!")
    return run

def main():
    """Execute multiple example experiments"""
    
    print("AIM Stack - Practical Examples")
    print("=" * 40)
    
    try:
        # Run different experiment types
        runs = []
        
        print("\n1️⃣ Basic Experiment")
        runs.append(basic_experiment())
        
        print("\n2️⃣ Image Experiment") 
        runs.append(advanced_experiment_with_images())
        
        print("\n3️⃣ Text Experiment")
        runs.append(experiment_with_text())
        
        print("\n" + "=" * 40)
        print("✅ All experiments completed!")
        print(f"📊 Total runs created: {len(runs)}")
        print("\n🌐 To view results:")
        print("   aim up")
        print("   Visit: http://localhost:43800")
        
    except KeyboardInterrupt:
        print("\n⏹️ Experiments interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during execution: {e}")

if __name__ == "__main__":
    main()
