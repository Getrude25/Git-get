!DOCTYPE html>
<!-- This declares the document type as HTML5 -->
<html lang="en">
<!-- The html element is the root element, lang="en" specifies the language -->

<head>
    <!-- The head section contains metadata about the document -->
    
    <!-- Meta tag for character set - tells the browser how to interpret text -->
    <meta charset="UTF-8">
    
    <!-- Meta tag for display/viewport - makes the page responsive on mobile devices -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Title appears in the browser tab and search engine results -->
    <title>Beginner HTML Template - Learn Web Development</title>
</head>

<body>
    <!-- The body contains all visible content on the webpage -->
    
    <!-- Header section - typically contains site branding and navigation -->
    <header>
        <h2>Welcome to My First Website</h2>
        <p>Learning HTML step by step</p>
    </header>
    
    <!-- Main heading of the page -->
    <h1>Basic HTML Template for Beginners</h1>
    
    <!-- Paragraph with descriptive content -->
    <p>
        This is a simple HTML template designed for beginner web developers. 
        It demonstrates the essential HTML elements you need to know including 
        headings, paragraphs, forms, tables, images, and links. Each element 
        is properly structured and commented to help you understand how HTML works.
    </p>
    
    <!-- Registration form section -->
    <h2>User Registration Form</h2>
    <p>Fill out the form below to register:</p>
    
    <!-- Form element with action and method attributes -->
    <form action="#" method="post">
        <!-- Each input is wrapped in a paragraph for basic structure -->
        
        <p>
            <!-- Label element associates text with form controls -->
            <label for="fullname">Full Name:</label><br>
            <!-- Input type="text" creates a text input field -->
            <input type="text" id="fullname" name="fullname" required placeholder="Enter your full name">
        </p>
        
        <p>
            <label for="email">Email Address:</label><br>
            <!-- Input type="email" provides email validation -->
            <input type="email" id="email" name="email" required placeholder="Enter your email">
        </p>
        
        <p>
            <label for="phone">Phone Number:</label><br>
            <!-- Input type="tel" is for telephone numbers -->
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">
        </p>
        
        <p>
            <!-- Submit button to send form data -->
            <button type="submit">Register Now</button>
        </p>
    </form>
    
    <!-- Table section displaying user information -->
    <h2>Sample User Information</h2>
    <p>Here's a table showing common user data:</p>
    
    <!-- Table element for displaying structured data -->
    <table border="1">
        <!-- Table header section -->
        <thead>
            <tr>
                <!-- th elements are table headers -->
                <th>Name</th>
                <th>Email</th>
                <th>Phone Number</th>
            </tr>
        </thead>
        
        <!-- Table body section -->
        <tbody>
            <!-- Each tr element creates a table row -->
            <tr>
                <!-- td elements are table data cells -->
                <td>Getruda Vitus</td>
                <td>getrudavitus2000@email.com</td>
                <td>(255)626749879</td>
            </tr>
    <!-- Image section -->
    <h2>Featured Image</h2>
    <p>Below is an example of how to embed an image:</p>
    
    <!-- Image element with src, alt, width, and height attributes -->
    <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80" 
         alt="Person typing on a laptop computer at a wooden desk" 
         width="400" 
         height="300">
    
    <!-- External link section -->
    <h2>External Resources</h2>
    <p>Need to search for something? Use the link below:</p>
    
    <!-- Anchor element creates a hyperlink -->
    <!-- target="_blank" opens link in new tab -->
    <!-- rel="noopener noreferrer" provides security for external links -->
    <a href="https://google.com" target="_blank" rel="noopener noreferrer">
        Visit Google Search Engine
    </a>
    
    <!-- Footer section (optional but good practice) -->
    <hr>
    <footer>
        <p>© 2025 Beginner HTML Template. Created for learning purposes.</p>
    </footer>
    
</body>
</html>
