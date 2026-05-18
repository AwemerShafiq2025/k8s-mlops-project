variable "project_name" {
  type        = string
  default     = "mlops-k8s-deployment"
  description = "Project ka naam"
}

variable "environment" {
  type        = string
  default     = "dev"
  description = "Deployment environment"
}