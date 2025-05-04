# Downward API Example

This is a simple example application that demonstrates how to use the Kubernetes Downward API. The application reads various pieces of information about the pod it's running in and displays them in a JSON format.

## Features

The application reads the following information from the Downward API:

- Pod Name
- Pod Namespace
- Pod IP
- Node Name
- Service Account Name

## Building the Container

To build the container locally:

```bash
docker build -t downward-api-example .
```

## Running the Container

To run the container locally:

```bash
docker run downward-api-example
```

## Using with Kubernetes

To use this container in Kubernetes, you'll need to set up the Downward API environment variables in your pod specification. Here's an example of how to configure the environment variables:

```yaml
env:
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: POD_NAMESPACE
    valueFrom:
      fieldRef:
        fieldPath: metadata.namespace
  - name: POD_IP
    valueFrom:
      fieldRef:
        fieldPath: status.podIP
  - name: NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName
  - name: SERVICE_ACCOUNT
    valueFrom:
      fieldRef:
        fieldPath: spec.serviceAccountName
```

## Development

The application is written in Python and uses the following features:

- Environment variable access through `os.getenv()`
- JSON formatting for output
- Continuous monitoring with 10-second intervals

## GitHub Actions

This repository includes a GitHub Actions workflow that automatically builds the container on push to main and pull requests. The workflow:

1. Sets up Docker Buildx
2. Builds the container
3. Uses GitHub Actions cache for faster builds

## License

MIT
