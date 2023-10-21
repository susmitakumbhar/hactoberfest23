<?php 

    $server = 'localhost';
    $user = "root";
    $password = "";
    $database = "viva";

    $conn = mysqli_connect($server, $user, $password, $database);

    if(!$conn)
    {
        echo "connection unsuccessfull";
    }

    if(isset($_POST['submit']))
    {
        $uname = $_POST['username'];
        $upassword = $_POST['userpassword'];
        $uemail = $_POST['useremail'];
        
        // users table

        $query = "INSERT INTO `users` (`name`, `password`, `email`) VALUES('$uname', '$upassword', '$uemail')";

        $result = $conn->query($query);
        header("Location: index.php");
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <style>
        .nclass{
        background-color: blue; 
        color:white;
        }
        .atag{
            text-decoration: none;
            width: 100px;
            padding: 5px 10px;
            background-color: beige;
            color: rgb(233, 7, 7);
            border: 1px solid black;
            border-radius: 12px;
        }

        .atag:hover{
            cursor:grab;
            color: rgb(233, 7, 7);
            background-color: white;
        }
        table{
            background-color: blue;
            color: white;
            text-align: center;
        }
        th{
            color: red;
            font-size: x-large;
            padding: 2px 5px;
        }
        form{
            background-color: antiquewhite;
            padding: 50px 200px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            text-align: center;
            margin: 0px auto;
        }

        form > input:not([type='submit']){
            width: 200px;
        }
        form > input[type='submit']{
            width: 100px;
        }
    </style>
</head>
<body>
    <form action="" method="post">
        <input required type="text" name = "username" placeholder="Enter Name here">
        <input required type="email" name="useremail" id="" placeholder="Enter Email here">
        <input required type="password" name="userpassword" id="" placeholder="Enter password here">
        <input class="nclass" required type="submit" name = "submit" value="signup">
    </form>

    <table border="1">
        <tr>
            <th>Sr.</th>
            <th>Name</th>
            <th>Email</th>
            <th>Password</th>
            <th>Action</th>
        </tr>

        <?php 
            $query12 = "SELECT * from `users`";
            $result = $conn->query($query12);
            if(mysqli_num_rows($result) > 0)
            {
                $sr = 1;
                foreach($result as $user)
                {
                ?>
                    <tr style="background-color: black;">
                        <td><?php echo $sr++; ?></td>
                        <td><?php echo $user['name']; ?></td>
                        <td><?php echo $user['email']; ?></td>
                        <td><?php echo $user['password']; ?></td>
                        <td>None</td>
                    </tr>
                <?php
                }
            }
        
        ?>
    </table>

        <button style="background-color: black;" class = "atag" >Click me</button>
        <input style="background-color: black;" class = "atag" type="button" value="Click Me">
        <input style="background-color: black;" class = "atag" type="submit" value="Click Me">
        <a style="background-color: black;" href="">Click Me</a>

</body>
</html>
