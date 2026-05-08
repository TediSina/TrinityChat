import json

from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ChatMessage, ChatSession


@override_settings(ALLOWED_HOSTS=["testserver"])
class DashboardViewTests(TestCase):
    def test_dashboard_renders_without_sessions(self):
        response = self.client.get(reverse("operator_dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Operator Dashboard")

    def test_session_status_endpoint_reports_human_mode(self):
        ChatSession.objects.create(session_id="session-1", is_human=True)

        response = self.client.post(
            reverse("get_session_status"),
            data=json.dumps({"session_id": "session-1"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_human": True})

    def test_chatbot_returns_response_when_session_is_human(self):
        ChatSession.objects.create(session_id="session-1", is_human=True)

        response = self.client.post(
            reverse("chatbot"),
            data=json.dumps({"session_id": "session-1", "message": "Hello"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["escalated"], True)
        self.assertEqual(ChatMessage.objects.filter(session_id="session-1").count(), 1)
