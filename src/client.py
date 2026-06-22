import grpc
import task_pb2
import task_pb2_grpc

def run():
    print("Connecting to server...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = task_pb2_grpc.TaskManagerStub(channel)
        
        print("----Get Task----")
        get_req = task_pb2.GetTaskRequest(id=1)
        task = stub.GetTask(get_req)
        print(f"Retrieved task: {task.title}")
        
        print("----Create Task----")
        create_req = task_pb2.CreateTaskRequest(title="Test title")
        new_task = stub.CreateTask(create_req)
        print(f"Created task: {new_task}")
        
        print("----List Tasks----")
        list_req = task_pb2.ListTaskRequest()
        all_tasks = stub.ListTasks(list_req)
        print("All tasks:")
        [print(f"- {task}") for task in all_tasks.tasks]
    
if __name__=="__main__":
    run()