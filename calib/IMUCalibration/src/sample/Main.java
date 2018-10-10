package sample;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class Main extends Application implements DataListener
{
    private TextArea logTextArea;
    private ScrollPane panelScrollPane;
    private GraphPanel graphPanel;
    private GridPane gridPane;
    private int graphIndex = 0;

    public static void main(String[] args)
    {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws Exception
    {
        gridPane = new GridPane();
        logTextArea = new TextArea();
        panelScrollPane = new ScrollPane();

        VBox box = new VBox();
        box.getChildren().add(panelScrollPane);
        VBox.setVgrow(panelScrollPane, Priority.ALWAYS);

        primaryStage.setScene(new Scene(box, 1200, 900));
        primaryStage.setTitle("IMU calibrations");
        primaryStage.show();

        gridPane.add(logTextArea, 1, 0);

        panelScrollPane.setContent(gridPane);

        setupSerialData();
    }

    private GridPane createACalibrationPanel(String title )
    {
        graphPanel = new GraphPanel();
        GridPane gridPane = new GridPane();
        gridPane.add(new Label(title), 0, 0);
        gridPane.add(graphPanel.getGraphPanel(), 0, 1);

        graphIndex++;

        return gridPane;
    }

    private void setupSerialData()
    {
        SerialClass serialClass = new SerialClass();
        serialClass.setDataListener(this);
    }


    @Override
    public void onDataAvailable(String s)
    {
        System.out.println("");
    }

    private void addGraphToThePanel()
    {
        GridPane p = createACalibrationPanel("test");
        gridPane.add(p, 0, graphIndex);
    }
}
