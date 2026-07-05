
def process_devops_tasks(tasks):
    """
    A simple function to loop through a list of tasks
    and separate them based on their status.
    """
    completed = []
    pending = []
    
    for task, is_done in tasks.items():
        if is_done:
            completed.append(task)
        else:
            pending.append(task)
            
    return completed, pending

# --- Main Program Execution ---
if __name__ == "__main__":
    # A dictionary sample representing tasks and their completion status
    assessment_tasks = {
        "Configure Ubuntu VM": True,
        "Fix Gedit Text Editor Warnings": True,
        "Set up Git Personal Access Token": True,
        "Write CI/CD Pipeline Automation": False,
        "Deploy Docker Container": False
    }
    
    # Unpacking the returned tuples from our function
    done, to_do = process_devops_tasks(assessment_tasks)
    
    print("✅ Completed Tasks:")
    for task in done:
        print(f"  - {task}")
        
    print("\n⏳ Pending Tasks:")
    for task in to_do:
        print(f"  - {task}")
