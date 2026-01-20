from locust import HttpUser, task, between

class EventsUser(HttpUser):
    """Simulates users browsing events."""
    
    wait_time = between(1, 2)
    user = "locust_user"

    @task
    def view_events(self):
        """Fetch and display available events."""
        self.client.get(f"/events?user={self.user}")
