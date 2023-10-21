<?php 
    $server = "localhost";
    $user = "root";
    $password = "";
    $db = "viva";
    $conn = mysqli_connect($server, $user, $password, $db);
    $fname=$lname='';
    if(!$conn)
    {
        echo "ERROR=>>>" . mysqli_connect_error();
    }

    if(isset($_GET['edit']))
    {
        $id = $_GET['edit'];
        $query = "SELECT * FROM `students` WHERE `id` = '$id'";
        $result = $conn->query($query);

        if(mysqli_num_rows($result) > 0)
        {
            $student = mysqli_fetch_assoc($result);
            $fname = $student['firstname'];
            $lname = $student['lastname'];
        }
    }

    if(isset($_POST['mysubmitbutton']))
    {
        $fname = $_POST['firstname'];
        $lname = $_POST['lastname'];

        if(isset($_GET['edit']))
        {
            $id = $_GET['edit'];
            $query = "UPDATE `students` SET `firstname` = '$fname', 
            `lastname` = '$lname' WHERE `id` = '$id'";
        }
        else
        {
            $query = "INSERT INTO `students`(`firstname`, `lastname`) 
            VALUES('$fname', '$lname')";
        }

        $result = $conn->query($query);
        if($result)
        {
            echo 
            '<script>
                alert("Success!");
                window.location.replace("index.php");
            </script>';
        }


    }
    $query = "SELECT * FROM `students`";
    $result = $conn->query($query);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./public/style/style.css">
    <title>Viva</title>
</head>
<body>
    <center >
        <form action="" method="post">
            <h1>Add new Form</h1>
            <input value = "<?php echo $fname;?>" name = "firstname" type="text" placeholder='Enter Your First Name'>
            <input value = "<?php echo $lname;?>" name = "lastname" type="text" placeholder='Enter Your Last Name'>
            <button name = "mysubmitbutton">Send Name Button</button>
        </form>

        <table border="1">
            <tr>
                <th>Sr</th>
                <th>FName</th>
                <th>LName</th>
                <th>Action</th>
            </tr>
        <?php 
            foreach($result as $student)
            {
        ?>
            <tr>
                <td>
                    <?php echo $student['id'];?>
                </td>
                <td>
                    Mr. <?php echo $student['firstname'];?>
                </td>
                <td>
                    <?php echo $student['lastname'];?>
                </td>
                <td>
                    <a href="?edit=<?php echo $student['id'];?>">Edit</a>
                    <a href="?del=<?php echo $student['id'];?>"> Del</a>
                </td>
            </tr>
        <?php 
            }
        ?>    
        </table>
    </center>

</body>
</html>

<?php 
    if(isset($_GET['del']))
    {
        $id = $_GET['del'];
        $query = "DELETE FROM `students` WHERE `id` = '$id'";

        $result = $conn->query($query);

        echo 
            '<script>
                alert("Student Deleted Successfully!");
                window.location.replace("index.php");
            </script>';
    }
?>
