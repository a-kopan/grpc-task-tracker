import grpc
from concurrent import futures
import task_pb2
import task_pb2_grpc
from db import *
from db import Task as DbTask

class Server(task_pb2_grpc.TaskManagerServicer):
    def __init__(self):
        self.engine = engine()
        
    def GetTask(self, request, context):
        db_results = get_task(self.engine, request.id)
        
        if not db_results:
            context.abort(grpc.StatusCode.NOT_FOUND, "Task not found")
        db_task = db_results[0]
        
        return task_pb2.Task(id=db_task.id, title=db_task.title, completed=db_task.completed)
        
    def CreateTask(self, request, context):
        new_db_task = DbTask(title=request.title, completed=False)
        create_task(self.engine, new_db_task)
        return task_pb2.Task(id=00, title=request.title, completed=False)

    def ListTasks(self, request, context):
        titles = list_tasks(self.engine)
        
        proto_tasks = []
        for i, title in enumerate(titles):
            proto_tasks.append(task_pb2.Task(id=i, title=title, completed=False))
            
        return task_pb2.ListTasksResponse(tasks=proto_tasks)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    my_server = Server()
    task_pb2_grpc.add_TaskManagerServicer_to_server(my_server, server)
    if is_empty(my_server.engine): 
        populate_db(my_server.engine)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051. Waiting for client...")
    server.wait_for_termination()
    
if __name__=="__main__":
    serve()