import json
from unittest.mock import Mock, patch

from django.test import SimpleTestCase, override_settings
from django.urls import reverse



@override_settings(ALLOWED_HOSTS=["testserver"])
class DashboardViewTests(SimpleTestCase):
    def test_dashboard_renders_without_sessions(self):
        response = self.client.get(reverse("operator_dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Operator Dashboard")

    def test_chat_page_has_new_chat_button(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Chat")

    def test_session_status_endpoint_is_database_free(self):
        response = self.client.post(
            reverse("get_session_status"),
            data=json.dumps({"session_id": "session-1"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_human": False})

    def test_chatbot_returns_response_when_browser_session_is_human(self):
        response = self.client.post(
            reverse("chatbot"),
            data=json.dumps({"message": "Hello", "is_human": True}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["escalated"], True)

    @patch("chat.views.model")
    def test_chatbot_uses_browser_history_without_database(self, mock_model):
        mock_model.generate_content.return_value = Mock(text="Your order is on the way.")

        response = self.client.post(
            reverse("chatbot"),
            data=json.dumps({
                "message": "Where is my order?",
                "order_history": "Order #1: pizza",
                "history": [{"sender": "user", "message": "Where is my order?"}],
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "response": "Your order is on the way.",
            "escalated": False,
        })
