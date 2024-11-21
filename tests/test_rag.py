import unittest
from rag import generate_response

class TestRAGPipeline(unittest.TestCase):
    def test_generate_response_without_rag(self):
        response = generate_response("What is the capital of France?", use_rag=False)
        self.assertIn("Paris", response)

    def test_generate_response_with_rag(self):
        response = generate_response("Explain quantum mechanics briefly.", use_rag=True)
        self.assertGreater(len(response), 10)  # Vérifie si une réponse est générée


if __name__ == "__main__":
    unittest.main()
