/* Customized command to show the click on the element */
Cypress.Commands.add('showClickCoordinates', (element, x, y) => {
  cy.wrap(element).then(($el) => {
    /* Reference - https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect */
    const rect = $el[0].getBoundingClientRect();

    cy.window().then((win) => {
      /* Create a new dot element*/
      const dot = win.document.createElement('div');
      dot.style.position = 'absolute';
      dot.style.width = '10px';
      dot.style.height = '10px';
      dot.style.backgroundColor = 'red';
      dot.style.borderRadius = '50%';
      dot.style.zIndex = '9999';

      /* Adjust the top and left coordinates to be relative to the element */
      dot.style.top = `${rect.top + y}px`;
      dot.style.left = `${rect.left + x}px`;

      /* Append the dot to the body */
      win.document.body.appendChild(dot);

      /* Remove the dot after 3 seconds */
      setTimeout(() => {
        dot.remove();
      }, 3000);
    });
  });
});

/* Generate Random Coordinates */
const getRandomCoordinates = (canvasWidth, canvasHeight, 
    left, top, canvas_center_x, canvas_center_y) =>
  {
      let randomX = Math.floor(Math.random() * (canvasWidth)) + left + 200;
      let randomY = Math.floor(Math.random() * (canvasHeight)) + top + 200;

      /* Adjust coordinates if they are outside the viewport size */
      if (randomX >= canvasWidth) {
         randomX = canvas_center_x
      }
  
      if (randomY >= canvasHeight) {
         randomY = canvas_center_y
      }
      
      return { randomX, randomY };
  };

describe('Bug Smasher Canvas Automation', () => {
  before(() =>
  {
    /* Set the viewport size to 1024 * 768 */
    cy.viewport(1024, 768);

    cy.visit('https://www.lambdatest.com/bug-smasher');

    /* Wait till the DOM contents are loaded */
    /* in this case, it is only the canvas element */
    cy.document().should((doc) => {
      expect(doc.readyState).to.equal('complete');
    });
    
    /* Additional cushioning for page loading */
    cy.wait(10000);
  });

  it('Bug Smasher Game Automation', () => {
    /* Print the viewport dimensions */
    cy.window().then((win) => {
      let viewportWidth = win.innerWidth;
      let viewportHeight = win.innerHeight;
      cy.log(`Viewport dimensions: ${viewportWidth} x ${viewportHeight}`);
    });

    /* Fetch canvas element details for interactions */
    cy.get('#unity-canvas').then(($canvas) => {
      const canvasWidth = $canvas[0].width;
      const canvasHeight = $canvas[0].height;
      cy.log(`Canvas width: ${canvasWidth}, Canvas height: ${canvasHeight}`);

      /* @hjsblogger - optional */
      const canvasOffset = $canvas.offset();
      cy.log(`Canvas offset top: ${canvasOffset.top}, Canvas offset left: ${canvasOffset.left}`)

      cy.wait(9000);

      const canvasRect = $canvas[0].getBoundingClientRect();
      const canvasX = canvasRect.x;
      const canvasY = canvasRect.y;

      const left = canvasRect.left;   /* 32 */
      const top = canvasRect.top;     /* 90 */
      const right = canvasRect.right; /* 992 */
      const bottom = canvasRect.bottom; /* 690 */

      cy.log(`Canvas X: ${canvasX}, Canvas Y: ${canvasY}`);

      cy.log(`Top: `, canvasRect.top);
      cy.log(`Right: `, canvasRect.right);
      cy.log(`Bottom: `, canvasRect.bottom);
      cy.log(`Left: `, canvasRect.left);
      cy.log(`Width: `, canvasRect.width);
      cy.log(`Height: `, canvasRect.height);
      cy.log(`X: `, canvasRect.x);
      cy.log(`Y: `, canvasRect.y);

      // Scale factor due to the canvas being scaled in CSS
      let canvasDisplayedWidth = canvasRect.width;
      let canvasDisplayedHeight = canvasRect.height;

      /* @hjsblogger */
      let canvasActualWidth = (canvasDisplayedWidth * 2);
      let scaleFactor = canvasDisplayedWidth / (canvasActualWidth);

      let canvasCenterX = (canvasDisplayedWidth / 2);
      let canvasCenterY = (canvasDisplayedHeight / 2);

      let buttonXInCanvas = (canvasCenterX * 2);
      /* This value also worked, but there is a better way out */
      /* let buttonYInCanvas = (canvasCenterY * 3); */
      let buttonYInCanvas = (canvasCenterY * 2)

      /* @hjsblogger - Click Working (1024 * 768) */
      /* const buttonXInCanvas = 936; */
      /* const buttonYInCanvas = 788 + 140; */

      /* Apply scale factor */
      let buttonXInCanvasScaled = buttonXInCanvas * scaleFactor;
      /* This value also worked, but there is a better way out */
      /* let buttonYInCanvasScaled = buttonYInCanvas * scaleFactor; */
      let buttonYInCanvasScaled = buttonYInCanvas;

      cy.log(`Button X (Scaled): ${buttonXInCanvasScaled}, 
          Button Y (Scaled): ${buttonYInCanvasScaled}`);

      /* Show Red Dot at the center of the canvas */
      cy.wrap($canvas)
      .then(() => {
        cy.showClickCoordinates($canvas, canvasCenterX,
            canvasCenterY);
      });

      cy.wait(1200);

      /* Position of the Play Now Button, it also depends on the viewport size */
      let clickX = canvasX + buttonXInCanvasScaled;
      /* This value also worked, but there is a better way out */
      /* let clickY = canvasY + buttonYInCanvasScaled; */
      /* Double Center of CanvasY and negate top (89.5) from it */
      let clickY = (buttonYInCanvasScaled - canvasY);

      cy.log(`Click X: ${clickX}, Click Y: ${clickY}`);

      /* Scroll into view and click at the calculated position inside the canvas */
      /* @hjsblogger - Check */
      // cy.get('canvas').scrollIntoView();
      cy.wait(1200);

      cy.wrap($canvas)
        .click(clickX, clickY, { force: true })
        .then(() => {
          cy.showClickCoordinates($canvas, clickX, clickY);
      });

      cy.wait(1200);

      cy.log('Clicked Play Now button');
      
      /* Perform 60 random clicks every 30 seconds */
      for (let cnt = 0; cnt < 60; cnt++)
      {
          const { randomX, randomY } = getRandomCoordinates(canvasWidth, canvasHeight,
                canvasRect.top, canvasRect.left, canvasCenterX, canvasCenterY);

          /* Log the X & Y coordinates */ 
          cy.log(`Clicking at X: ${randomX}, Y: ${randomY}`);

          /* @hjsblogger - Interact with the canvas element */
          /* cy.get('#unity-canvas').click(); */

          /* Perform a force click */
          /* https://docs.cypress.io/app/core-concepts/interacting-with-elements#Forcing */

          const clicked_xpos = randomX - canvasRect.left;
          const clicked_ypos = randomY - canvasRect.top;

          cy.wrap($canvas)
            .click(clicked_xpos,clicked_ypos, { force: true })
            .then(() => {
              /* Show the dot at the clicked position */
              cy.showClickCoordinates($canvas, clicked_xpos,
                (clicked_ypos));
            });

          /* Add delay to visualize the clicks */
          cy.wait(500);
      }
    });
    cy.log('Canvas Game Testing Complete')

    cy.wait(4000);

    /* Now click on LinkedIn Button which is outside the Canvas */
    /* Stub the window.open method */
    cy.window().then((win) =>
    {
      cy.stub(win, 'open').as('windowOpen'); // Stubbing window.open
    });

    /* Locate LinkedIn button and click on it */
    cy.get('#unity-container > div.share-list > a.li-h').click();

    /* Verify that window.open was called with a URL containing 'linkedin.com' */
    cy.get('@windowOpen').should('be.calledWith', 
        Cypress.sinon.match.string.and(Cypress.sinon.match('linkedin.com')));

    cy.wait(10000);

    cy.log('LinkedIn - Button Clicked')
  });
});

/*
const socialMediaTest = Cypress.env('SOCIAL_MEDIA_TEST');

if (socialMediaTest)
{
  describe('Social Media Links Test', () => {
    before(() => {
      cy.viewport(1024, 768);

      // Load the URL and wait for it to fully load
      cy.visit('https://www.lambdatest.com/bug-smasher');
      cy.wait(5000); // Wait for 5 seconds to allow the page to load
    });

    it('LinkedIn Link Click Test', () => {
      // Add delay to ensure everything is ready
      cy.wait(5000);
    
      // Stub the window.open method
      cy.window().then((win) => {
        cy.stub(win, 'open').as('windowOpen'); // Stubbing window.open
      });

      // Click the button that opens the new window
      cy.get('#unity-container > div.share-list > a.li-h').click();

      // Verify that window.open was called with a URL containing 'linkedin.com'
      cy.get('@windowOpen').should('be.calledWith',
          Cypress.sinon.match.string.and(Cypress.sinon.match('linkedin.com')));

      cy.wait(10000);

      cy.log('Canvas Game Testing Complete - 2')

    });
  });
}
*/
