resource "kubernetes_namespace" "mlops_space" {
  metadata {
    name = "${var.project_name}-${var.environment}"
  }
}