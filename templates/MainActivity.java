package com.mediaserver.pro;

import android.app.*;
import android.os.*;
import android.widget.*;
import android.view.*;
import java.io.*;
import java.net.*;
import java.util.*;

public class MainActivity extends Activity {
    
    private TextView statusText;
    private Button startBtn, stopBtn;
    private WebServer server;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        statusText = findViewById(R.id.statusText);
        startBtn = findViewById(R.id.startBtn);
        stopBtn = findViewById(R.id.stopBtn);
        
        startBtn.setOnClickListener(v -> startServer());
        stopBtn.setOnClickListener(v -> stopServer());
        
        updateUI(false);
    }
    
    private void startServer() {
        try {
            server = new WebServer(8080);
            server.start();
            updateUI(true);
            Toast.makeText(this, "Server started", Toast.LENGTH_SHORT).show();
        } catch (IOException e) {
            Toast.makeText(this, "Failed to start server", Toast.LENGTH_SHORT).show();
        }
    }
    
    private void stopServer() {
        if (server != null) {
            server.stopServer();
            server = null;
        }
        updateUI(false);
        Toast.makeText(this, "Server stopped", Toast.LENGTH_SHORT).show();
    }
    
    private void updateUI(boolean running) {
        statusText.setText(running ? "RUNNING" : "STOPPED");
        statusText.setTextColor(running ? 0xFF4CAF50 : 0xFFF44336);
        startBtn.setEnabled(!running);
        stopBtn.setEnabled(running);
    }
    
    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (server != null) {
            server.stopServer();
        }
    }
}

class WebServer extends Thread {
    private ServerSocket serverSocket;
    private boolean isRunning = false;
    private int port;

    public WebServer(int port) throws IOException {
        this.port = port;
        this.serverSocket = new ServerSocket(port);
    }

    @Override
    public void run() {
        isRunning = true;
        while (isRunning) {
            try {
                Socket clientSocket = serverSocket.accept();
                handleClient(clientSocket);
            } catch (IOException e) {
                if (isRunning) e.printStackTrace();
            }
        }
    }
    
    public void stopServer() {
        isRunning = false;
        try {
            if (serverSocket != null) serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    private void handleClient(Socket clientSocket) {
        try {
            BufferedReader in = new BufferedReader(
                new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            
            String request = in.readLine();
            if (request != null && request.startsWith("GET")) {
                String html = "<html><body><h1>Media Server Pro</h1><p>Running on Android</p></body></html>";
                out.println("HTTP/1.1 200 OK");
                out.println("Content-Type: text/html");
                out.println("Content-Length: " + html.length());
                out.println();
                out.println(html);
            }
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
