from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    """Simulates users viewing their registered events."""
    
    wait_time = between(1, 2)
    user = "locust_user"

    @task
    def view_my_events(self):
        """Fetch and display user's registered events."""
        self.client.get(f"/my-events?user={self.user}")
